# Assignment 4

제출기한: 22.11.27(일) 23:59:59

## 안내


## problem 1: render.com을 이용한 production 배포

paas 플랫폼인 render.com을 이용해 django project를 배포합니다.

- `settings.py debug=false` 로 설정되어야 합니다.
- '/' 로 접근시 status 200과 함께 f"hello ${name}!"이 출력됩니다.

![예시](./%EC%98%88%EC%8B%9C.png) 

### 제출
- 기존과 같이 해당 repository의 root에 django project를 업로드해주세요.
- 해당 repo를 fork 한 후, Pull request 요청합니다.
- PR 내용에 접근 가능한 url을 제공해주세요. (예시: https://render-django-vzf1.onrender.com/)

## problem 2: render.com을 이용한 custom management command cron job

custom management command를 작성한 후, 이를 render.com의 cronjob을 이용해 scheduled로 실행합니다.

- management command는 어떤 일을 해도 상관없습니다. `print(f"${name}")` 등으로 로그를 확인할 수 있게 해주세요.
- cronjob 문법을 이용해, **매일 한 번씩 자정** 에 실행될 수 있도록 cronjob을 설정합니다.


### 제출
- 설정 완료된 cronjob 페이지의 스크린샷을 repository root에 첨부해주세요.
