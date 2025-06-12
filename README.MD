# Agent Server

## Hexagonal Architecture

이 프로젝트는 헥사고날 아키텍처(포트와 어댑터 패턴)를 기반으로 설계된 에이전트 서버입니다.

### 프로젝트 구조

```
.
├── app/                    # 애플리케이션 핵심 코드
│   ├── adapter/           # 외부 시스템과의 통신을 담당하는 어댑터
│   ├── application/       # 유스케이스 및 애플리케이션 서비스
│   ├── configurator/      # 의존성 주입 및 설정 관리
│   ├── domain/           # 도메인 모델 및 비즈니스 로직
│   └── main.py           # 애플리케이션 진입점
├── prisma/               # Prisma ORM 설정 및 스키마
├── main.py              # 서버 진입점
├── pyproject.toml       # 프로젝트 의존성 및 설정
├── poetry.lock         # 의존성 잠금 파일
├── docker-compose.yml  # Docker 컨테이너 설정
└── Makefile           # 프로젝트 빌드 및 실행 명령어
```

### 기술 스택

- **언어**: Python 3.13
- **웹 프레임워크**: FastAPI
- **ORM**: Prisma
- **의존성 관리**: Poetry
- **인증**: Argon2, JWT
- **AI/ML**: OpenAI, LangChain, LangGraph
- **개발 도구**: Black, Flake8, isort

### 주요 기능

- FastAPI 기반의 RESTful API 서버
- 헥사고날 아키텍처를 통한 관심사 분리
- 의존성 주입을 통한 결합도 감소
- Prisma ORM을 통한 데이터베이스 관리
- OpenAI와 LangChain을 활용한 AI 에이전트 기능
- SSE(Server-Sent Events)를 통한 실시간 통신

### 개발 환경 설정

1. Poetry 설치

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

2. 의존성 설치

```bash
poetry install
```

3. 환경 변수 설정

```bash
cp .env.example .env
# .env 파일을 편집하여 필요한 환경 변수 설정
```

4. 데이터베이스 마이그레이션

```bash
poetry run prisma migrate dev
```

### 실행 방법

개발 서버 실행:

```bash
poetry run uvicorn main:app --reload
```

Docker를 통한 실행:

```bash
docker-compose up
```

### 테스트

```bash
poetry run pytest
```

### 코드 스타일

- Black을 사용한 코드 포맷팅
- Flake8을 사용한 린팅
- isort를 사용한 import 정렬

### 라이선스

이 프로젝트는 MIT 라이선스 하에 배포됩니다.
