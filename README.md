# Wanted X Wecode 백엔드 프리온보딩 선발 과제

## 💻 사용 기술 : Python, Django
## 💻 구현 방법과 이유
 1. User와 Post로 App을 나누어 기능을 구현하였습니다.
 2. Restful API를 사용했습니다.
 3. User 계정 생성/ 로그인 시 bcrypt, jwt를 통해 인증/인가를 구현하였습니다.
 4. Post의 Pagination을 활용하여 한 페이지에 3개씩 게시글이 표출되게 하였습니다.
 5. Unit Test를 진행해 로직을 검증하였습니다.

<hr>

## 💻 ENDPOINT 호출방법
<img width="592" alt="스크린샷 2021-10-27 오전 1 38 15" src="https://user-images.githubusercontent.com/81546305/138923086-c8fbe183-710d-46bf-899f-4ea7831ac7ae.png">
python manage.py runserver 명령어를 통해 localhost:8000에서 실행할 수 있습니다.

## 💻 API 명세서
<img width="468" alt="스크린샷 2021-10-27 오전 1 44 14" src="https://user-images.githubusercontent.com/81546305/138923930-67fac225-8856-4374-afe1-19f64e5b7b21.png">

## ☑️ 각 기능 별 request/response

### 👉🏻 계정 생성
<br>
<img width="491" alt="스크린샷 2021-10-27 오전 12 41 22" src="https://user-images.githubusercontent.com/81546305/138924233-fdd22c73-2d6c-4008-aefe-94d68508fc0a.png">

### 👉🏻 로그인
<br>
<img width="815" alt="스크린샷 2021-10-27 오전 12 41 47" src="https://user-images.githubusercontent.com/81546305/138924275-1d4cc96d-ce23-4e5c-ae5b-b5b4cdfd5de2.png">
 
### 👉🏻 게시글 생성
<br>
<img width="487" alt="스크린샷 2021-10-27 오전 1 55 48" src="https://user-images.githubusercontent.com/81546305/138925608-44c5bc08-8d0d-4a21-a4ef-d3e23d2a5d57.png">

### 👉🏻 게시글 조회 _ Pagination 진행
<br>
<img width="781" alt="스크린샷 2021-10-26 오후 11 26 30" src="https://user-images.githubusercontent.com/81546305/138925122-59ac5c95-87f9-4ee2-9079-822200ae480e.png">

### 👉🏻 게시글 수정
<br>
<img width="463" alt="스크린샷 2021-10-26 오후 10 57 21" src="https://user-images.githubusercontent.com/81546305/138925190-04a6e81f-d784-413e-a5ce-48a2724429d4.png">

### 👉🏻 게시글 삭제
<br>
<img width="555" alt="스크린샷 2021-10-26 오후 10 57 52" src="https://user-images.githubusercontent.com/81546305/138924403-1ca367c4-8d62-41f0-9e20-7cded1af298e.png">

<hr>

## 💻 Unit Test 결과

### 테스트 4개 진행 
### [User Test 2개 : 계정 생성 성공 / 중복 오류 , Post Test 2개 : 게시글 조회 성공 / 게시글 조회 에러]
<br>
<img width="385" alt="스크린샷 2021-10-27 오전 12 38 31" src="https://user-images.githubusercontent.com/81546305/138924788-d5ef4d1b-cd97-4a1d-bf51-8092abc39d67.png">

