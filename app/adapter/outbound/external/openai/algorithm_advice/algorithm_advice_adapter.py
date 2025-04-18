from operator import itemgetter
from typing import AsyncGenerator

from langchain.memory.summary_buffer import ConversationSummaryBufferMemory
from langchain.prompts import ChatPromptTemplate
from langchain.schema.runnable import RunnableLambda, RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI

from app.application.port.outbound.ai.algorithm_advice import (
    AlgorithmAdviceGeneratePort,
)


class AlgorithmAdviceAdapter(AlgorithmAdviceGeneratePort):

    def __init__(
        self,
    ) -> None:

        self._memory_llm = ChatOpenAI(
            temperature=0.1,
            model="gpt-3.5-turbo",
        )

        self._memory = ConversationSummaryBufferMemory(
            llm=self._memory_llm,
            max_token_limit=500,
            memory_key="chat_history",
            return_messages=True,
        )

    async def generate(self, email: str, lang: str, message: str) -> AsyncGenerator:

        prompt = ChatPromptTemplate.from_template(
            template="""For algorithm problems or specific situations, here's a structured approach to advising on algorithms and solving examples:
        Use the following language to solve the problem: {lang}
        user input is: {user_input}
        answer language: Korean

        IMPORTANT: If it is related to the previous question of the user's question, refer to the previous question and answer. If not, follow the following instructions.

        1. **Understand the Problem:** Clearly define and understand the problem statement. Identify the inputs, outputs, and any constraints or special conditions.
        2. **Choose the Appropriate Algorithm:** Based on the problem type, complexity, and constraints, select an algorithm or data structure that best fits. Consider time and space complexity, scalability, and the nature of the data.
        3. **Outline the Algorithm:** Provide a step-by-step description of how the algorithm works. This might include initializing variables, loops, conditionals, recursive calls, or the use of specific data structures.
        4. **Implement the Algorithm:** Write pseudocode or actual code that implements the algorithm. Ensure the code is clean, understandable, and well-commented. You should generate all logics details and You should generate code by using {lang}.
        5. **Test with Examples:** Use example inputs to test the algorithm. Include a variety of cases such as the general case, edge cases, and cases that test the limits of the algorithm.
        6. **Optimize and Refine:** Review the algorithm for potential optimizations. Consider edge cases or inputs that could cause the algorithm to fail or perform inefficiently and refine accordingly.
        7. **Discuss Time and Space Complexity:** Analyze and discuss the time and space complexity of the algorithm. Explain how the algorithm scales with the size of the input and any trade-offs made during the algorithm selection process.

        Example Problem: Given an array of integers, return the indices of the two numbers such that they add up to a specific target.

        1. Understand the Problem:
        - Input: An array of integers, and a target integer.
        - Output: Indices of the two numbers that add up to the target.
        2. Choose the Appropriate Algorithm:
        - A hash table can be used for efficient lookups to check for the existence of the complement (target - current number).
        3. Outline the Algorithm:
        - Initialize an empty hash table.
        - Iterate through the array:
            - For each element, check if the complement (target - element) exists in the hash table.
            - If it does, return the current index and the index of the complement from the hash table.
            - If it does not, add the current element and its index to the hash table.
        4. Implement the Algorithm:
        ```
        function twoSum(nums, target) {{
        let map = new Map();
        for (let i = 0; i < nums.length; i++) {{
            let complement = target - nums[i];
            if (map.has(complement)) {{
            return [map.get(complement), i];
            }}
            map.set(nums[i], i);
        }}
        return null;
        }}
        ```

        5. Test with Examples:
        - Input: nums = [2, 7, 11, 15], target = 9
        - Output: [0, 1] (Because nums[0] + nums[1] = 2 + 7 = 9)

        6. Optimize and Refine:
        - The current solution is efficient and handles all cases with a single pass through the array.

        7. Discuss Time and Space Complexity:
        - Time Complexity: O(n), where n is the number of elements in the array.
        - Space Complexity: O(n), due to the additional hash table.

        """
        )

        # LLM
        llm = ChatOpenAI(
            # model_name="gpt-4-0125-preview",
            model="gpt-3.5-turbo",
            temperature=0,
            max_tokens=1000,
        )  # 4000자

        # Chain
        chain = (
            {
                "user_input": itemgetter("user_input"),
                "lang": itemgetter("lang"),
            }
            | RunnablePassthrough.assign(
                chat_history=RunnableLambda(self._memory.load_memory_variables)
                | itemgetter("chat_history")
            )
            | prompt
            | llm
            | StrOutputParser()
        )

        response = ""
        async for token in chain.astream({"user_input": message, "lang": lang}):
            yield token
            response += token
        self._save_message(message, response)

    def _save_message(self, input, output):
        self._memory.save_context(inputs={"input": input}, outputs={"output": output})
