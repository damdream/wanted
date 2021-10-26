# Wanted X Wecode 백엔드 프리온보딩 선발 과제

## - 사용 기술 : Python, Django
## - 구현 방법과 이유
 1. User와 Post로 App을 나누어 기능을 구현하였습니다.
 2. Restful API를 사용했습니다.
 3. User 계정 생성/ 로그인 시 bcrypt, jwt를 통해 인증/인가를 구현하였습니다.
 4. Post의 Pagination을 활용하여 한 페이지에 3개씩 게시글이 표출되게 하였습니다.

## - ENDPOINT 호출방법
<img width="592" alt="스크린샷 2021-10-27 오전 1 38 15" src="https://user-images.githubusercontent.com/81546305/138923086-c8fbe183-710d-46bf-899f-4ea7831ac7ae.png">
python manage.py runserver 명령어를 통해 localhost:8000에서 실행할 수 있습니다.

## - API 명세서
<img width="468" alt="스크린샷 2021-10-27 오전 1 44 14" src="https://user-images.githubusercontent.com/81546305/138923930-67fac225-8856-4374-afe1-19f64e5b7b21.png">

## ☑️ 각 기능 별 request/response
