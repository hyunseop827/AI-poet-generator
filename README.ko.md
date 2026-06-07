# AI Poet Generator

[English README](README.md)

AI Poet Generator는 사용자가 입력한 주제를 바탕으로 한국어 시를 생성하는 간단한 Streamlit 웹 앱입니다. LangChain을 통해 OpenAI 모델을 호출하고, 짧은 주제를 시 형태의 텍스트로 바꿔주는 창작 보조 도구입니다.

## 프로젝트 성격

이 프로젝트는 AI 기반 창작 글쓰기 도구입니다. 복잡한 서비스보다는 다음 기술을 간단히 연결해 보는 데 초점을 둔 데모 애플리케이션입니다.

- Streamlit을 사용한 웹 인터페이스
- LangChain을 사용한 모델 연동
- OpenAI를 사용한 텍스트 생성
- 환경변수를 사용한 API 키 관리

## 주요 기능

- 한국어로 시의 주제 입력
- OpenAI 채팅 모델을 이용한 시 생성
- API 키 설정 여부 확인
- `python-dotenv`를 통한 로컬 `.env` 파일 지원

## 요구사항

- Python 3.11 이상
- OpenAI API 키

## 설치

의존성을 설치합니다.

```bash
pip install -r requirements.txt
```

프로젝트 루트에 `.env` 파일을 만듭니다. `.env.example` 파일을 참고할 수 있습니다.

```bash
OPENAI_API_KEY=your_openai_api_key_here
```

## 실행

Streamlit 앱을 실행합니다.

```bash
streamlit run main.py
```

이후 터미널에 표시되는 로컬 Streamlit 주소를 브라우저에서 열면 됩니다.

## 참고

이 앱은 기본적인 AI 글쓰기 흐름을 보여주기 위해 의도적으로 단순하게 구성되어 있습니다. 이후 시의 분위기, 길이, 문체, 모델 선택, 생성 기록 저장 같은 기능을 추가해 확장할 수 있습니다.
