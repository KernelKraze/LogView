**LogView 프로젝트 README**

📁 **프로젝트 구조**
```
📂 LogView
  ├── AuthView.py
  ├── KernelView.py
  ├── MongodbView.py
  ├── NginxErrorView.py
  ├── NginxView.py
  └── SysLogView.py
```

**AuthView.py**
```python
🔐 **인증 로그 뷰어**

- 이 모듈은 인증 로그를 처리합니다.
- 'sudo' 명령 사용과 실패한 SSH 로그인 시도를 감지합니다.
- 사용자 활동 및 실패한 로그인 세부 정보를 표시합니다.

**사용 방법:**
1. 해당 파일을 실행합니다.
2. 로그 파일 경로를 설정하고 인증 로그를 확인합니다.
3. 'sudo' 명령 사용과 SSH 로그인 시도를 분석하고 특정 사용자의 활동을 확인합니다.

```

**KernelView.py**
```python
🐧 **커널 로그 뷰어**

- 이 모듈은 커널 로그를 처리합니다.
- EXT4 파일 시스템 경고, 오류 및 저전압 경고를 캡처합니다.
- 집계된 로그 이벤트 및 발생 횟수를 표시합니다.

**사용 방법:**
1. 해당 파일을 실행합니다.
2. 커널 로그 파일의 경로를 설정하고 커널 이벤트를 검토합니다.
3. 로그에서 발생한 경고 및 오류를 식별하고 이러한 이벤트의 발생 빈도를 확인합니다.

```

**MongodbView.py**
```python
📦 **MongoDB 로그 뷰어**

- 이 모듈은 MongoDB 로그를 처리합니다.
- JSON 객체를 추출하고 로그 항목을 표시합니다.
- 타임스탬프, 레벨, 카테고리, 컨텍스트, 메시지 및 추가 속성을 제공합니다.

**사용 방법:**
1. 해당 파일을 실행합니다.
2. MongoDB 로그 파일의 경로를 설정하고 로그를 검토합니다.
3. JSON 객체를 추출하고 MongoDB 작업에 대한 세부 정보를 확인합니다.

```

**NginxErrorView.py**
```python
🚨 **Nginx 오류 로그 뷰어**

- 이 모듈은 Nginx 오류 로그를 처리합니다.
- 시간대, 레벨, 클라이언트 IP, 서버, 요청 메서드, 요청 URL, 메시지 및 참조자를 파싱합니다.
- 오류 세부 정보 및 IP 개수 요약을 표시합니다.

**사용 방법:**
1. 해당 파일을 실행합니다.
2. Nginx 오류 로그 파일의 경로를 설정하고 오류를 분석합니다.
3. 오류 발생 시간대, 클라이언트 IP 및 해당 오류에 대한 자세한 정보를 확인합니다.

```

**NginxView.py**
```python
🌐 **Nginx 액세스 로그 뷰어**

- 이 모듈은 Nginx 액세스 로그를 처리합니다.
- IP 주소, 타임스탬프, HTTP 메서드, URL, 상태 코드 및 사용자 에이전트를 파싱합니다.
- 액세스 세부 정보 및 IP 개수 요약을 표시합니다.

**사용 방법:**
1. 해당 파일을 실행합니다.
2. Nginx 액세스 로그 파일의 경로를 설정하고 로그를 검토합니다.
3. 사용자가 액세스한 URL, 상태 코드 및 사용자 에이전트와 같은 세부 정보를 확인합니다.

```

**SysLogView.py**
```python
📝 **시스템 로그 뷰어**

- 이 모듈은 시스템 로그를 처리합니다.
- 시간대, 프로세스, PID 및 메시지를 포함한 일반 시스템 로그 항목을 캡처합니다.
- 시스템 로그 메시지를 표시합니다.

**사용 방법:**
1. 해당 파일을 실행합니다.
2. 시스템 로그 파일의 경로를 설정하고 로그를 검토합니다.
3. 시스템 이벤트 및 프로세스 활동과 같은 로그 메시지를 확인합니다.

```

이 프로젝트는 다양한 로그 유형을 처리하고 분석하여 시스템의 상태를 이해하고 문제를 해결하는 데 도움이 됩니다. 각 모듈은 특정 유형의 로그에 대한 자세한 정보를 제공하고 사용자가 문제를 진단하고 해결할 수 있도록 도와줍니다.