
## 📘 Domain Relaxation (도메인 완화)

### 📌 개념 요약

**Domain Relaxation**은 브라우저의 보안 정책인 Same Origin Policy (SOP)를 부분적으로 완화하는 기술

> ❗ 기본 SOP 규칙  
> A 웹페이지가 B 웹페이지에 접근하려면  
> **scheme(프로토콜), domain, port**가 **모두 같아야** 한다.

그러나 실제 웹 서비스에서는 여러 서브도메인을 함께 사용할 일이 많죠. 예:

- `a.example.com`
- `b.example.com`

이런 경우, 서로 다른 서브도메인 간에 데이터를 공유하려면 브라우저는 접근을 막습니다.  
→ 그래서 나온 방식이 바로 **`document.domain`을 같게 설정하는 것**

---

### 🧪 예시 코드

```js
// a.example.com 과 b.example.com 각각에서 아래와 같이 설정
document.domain = "example.com";
```

→ 이렇게 하면 둘 다 **출처(origin)**가 `example.com`으로 동일해졌다고 간주하고,  
→ **DOM 접근, 쿠키 공유 등이 가능**해집니다.

---

### 🚨 보안상의 허점이 많다.

| 문제점 | 설명 |
|--------|------|
| ✅ 너무 완화됨 | 도메인 수준에서 느슨하게 출처를 통일시켜, 보안 경계가 무너짐 |
| ✅ iframe, 광고 등에서 악용 가능 | 서브도메인에 있는 악성 코드가 부모 사이트의 민감한 정보에 접근 가능 |
| ✅ Public Suffix List와 충돌 | `github.io`, `co.uk` 같은 공공 도메인에선 이 완화가 **심각한 보안 위협**으로 작용 |

#### 예를 들어:
- `user1.github.io` 와 `user2.github.io`가 `document.domain = "github.io"`를 하면?
- → **서로 다른 사용자의 웹사이트가 서로의 쿠키나 DOM에 접근**할 수 있게 된다.

---

## 🧱 Domain Relaxation 이후의 대응 기술

### ✅ 1. `postMessage()` — 안전한 메시지 전송
### ✅ 2. **CORS (Cross-Origin Resource Sharing)** — 서버 간 안전한 요청 허용
### ✅ 3. **Content Security Policy (CSP)** — 어떤 출처에서 어떤 콘텐츠를 허용할지 선언
### ✅ 4. Public Suffix List (PSL) — 허용 불가능한 도메인 구분
### ✅ 5. Origin isolation + SameSite 쿠키 - 탭/iframe 간 철저한 출처 분리 & 쿠키 보안 강화

---

## 사용법 : 🧩 `hosts` 파일 설정

우리가 `127.0.0.1 a.domain.test`처럼 쓰는 건, **가짜 도메인 주소를 만들어서 내 컴퓨터 안에서만 작동하게 하는 작업**. 이걸 통해 마치 실제 서버처럼 여러 도메인을 흉내 낼 수 있다.

---




- `a.domain.test`는 **첫 번째 가짜 도메인** (부모 페이지)
- `b.domain.test`는 **두 번째 가짜 도메인** (iframe 등 자식 페이지)

이 둘은 브라우저 기준에서 "다른 출처(origin)"로 인식된다.  
이렇게 하면 SOP(Same Origin Policy)가 어떻게 작동하는지를 실험할 수 있게 된다.



### ✅ 예를 들어 설명하면…

| 설정 내용 (`hosts`) | 실제 의미 |
|---------------------|------------|
| `127.0.0.1 a.domain.test` | `a.domain.test`는 내 컴퓨터에서 열어라 |
| `127.0.0.1 b.domain.test` | `b.domain.test`도 내 컴퓨터에서 열어라 |

이렇게 설정해두면, 내 컴퓨터에 `a.domain.test`와 `b.domain.test`라는 **서로 다른 주소**가 만들어진다.
그럼 브라우저 입장에서는:

> “어? 도메인이 다르네. 그럼 출처가 다르니까 접근 못 하게 해야지!”