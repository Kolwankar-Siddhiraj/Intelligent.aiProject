from django.shortcuts import render
import re

from django.urls.conf import path
#from django.http import HttpResponse 

# all global variables here 
otp_char_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a','A', 'b','B', 'c','C', 'd','D', 
                'e','E', 'f','F', 'g','G', 'h','H', 'i','I', 'j','J', 'k','K', 'l','L', 'm','M', 'n','N', 
                'o','O', 'p','P', 'q','Q', 'r','R', 's','S', 't','T', 'u','U', 'v','V', 'w','W', 'x','X', 'y','Y','z','Z']

regex_pattern_to_check_email = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
regex_pattern_to_check_name1 = "[a-z]"
regex_pattern_to_check_name2 = "[A-Z]"
regex_pattern_to_check_name3 = "[a-zA-Z]"
regex_pattern_to_check_otp = "[a-zA-Z0-9]"
regex_pattern_to_check_password = r'[A-Za-z0-9@#$%^&+=]{8,}'
#regex_pattern_to_check_password = re.compile("^(?=.[a-z])(?=.[A-Z])(?=.\d)(?=.[@$!%#?&])[A-Za-z\d@$!#%?&]{6,20}$")



# HTML tag check class
class html_info:
    login_button_name = str("Login")
    active_form_login = bool(True)


class form_error_messages: 
    # Error messages for login
    invalid_login_username = bool(False)
    invalid_login_password = bool(False)
    # Error messages for signup 
    invalid_signup_name_user = bool(False)
    invalid_signup_email = bool(False)
    invalid_signup_password = bool(False)
    invalid_signup_comfirm_password = bool(False)
    # Error messages for sign up OTP
    invalid_signup_otp = bool(False)


error_msg_form = form_error_messages() 
info_html = html_info()

# Create your views here.

def use_regular_expression(check_pattern, check_value):
    if re.fullmatch(check_pattern, check_value):
        return True
    else:
        return False


def reset_all_error_message():
    error_msg_form.invalid_login_username = False
    error_msg_form.invalid_login_password  = False
    error_msg_form.invalid_signup_name_user  = False
    error_msg_form.invalid_signup_email  = False
    error_msg_form.invalid_signup_password  = False
    error_msg_form.invalid_signup_comfirm_password  = False
    error_msg_form.invalid_signup_otp = False


def home(request):

    info_html.login_button_name = "Login"

    #return render(request, 'index.html')
    return render(request, 'index.html', {'info_html':info_html})


def login_or_signup(request):

    # check_clicked = str(request.path)
    # print(f"URL is :: {check_clicked}")

    # if check_clicked == "/login_or_signup":
    #     info_html.active_form_login = True
    # elif check_clicked == "/login":
    #     info_html.active_form_login = True
    # elif check_clicked == "/create_account":
    #     info_html.active_form_login = False
    # else:
    #     info_html.active_form_login = True

    info_html.active_form_login = True


    return render(request, 'login_signup_form.html', {'info_html':info_html})


def login(request):

    reset_all_error_message()
    info_html.active_form_login = True
    final_return_template = bool(False)

    login_username = str(request.POST["login_username"])
    login_password = str(request.POST["login_password"])
    
    print("Username :: " + login_username, " Password :: " + login_password)
    
    if use_regular_expression(regex_pattern_to_check_email, login_username):

        if use_regular_expression(regex_pattern_to_check_password, login_password):
            info_html.login_button_name = "Siddhiraj"
            final_return_template = True
            print("Valid Password!")
        else:
            error_msg_form.invalid_login_password = True
            final_return_template = False
            print("Invalid Password!")
    
        print("Valid Email!")
    else:
        error_msg_form.invalid_login_username = True 
        print("Invalid Email!")

    if final_return_template:
        return render(request, 'index.html', {'info_html':info_html} )
    else:
        return render(request, 'login_signup_form.html', {'info_html':info_html, 'error_msg_form':error_msg_form} )


def create_account(request):

    reset_all_error_message()
    info_html.active_form_login = False
    
    correct_name = bool(False)
    correct_email = bool(False)
    correct_password = bool(False)
    correct_confirm_password = bool(False)
    correct_both_password = bool(False)

    signup_name_user = str(request.POST["signup_name_user"])
    signup_email = str(request.POST["signup_email"])
    signup_password = str(request.POST["signup_password"])
    signup_confirm_password = str(request.POST["signup_confirm_password"])

    print(f"Name :: {signup_name_user} Email :: {signup_email} Password :: {signup_password} Confirm Password :: {signup_confirm_password}")

    # validate name of user
    #if use_regular_expression(regex_pattern_to_check_name1, signup_name_user) or use_regular_expression(regex_pattern_to_check_name2, signup_name_user) or use_regular_expression(regex_pattern_to_check_name3, signup_name_user) :
    if re.search('[a-zA-Z]', signup_name_user):
        correct_name = True
        print("Valid Name!")
    else:
        error_msg_form.invalid_signup_name_user = True
        correct_name = False
        print("Invalid Name!")
    

    # validate Email of user
    if use_regular_expression(regex_pattern_to_check_email, signup_email):
        correct_email = True
        print("Valid Email!")
    else:
        error_msg_form.invalid_signup_email = True
        correct_email = False
        print("Invalid Email!")


    if correct_name and correct_email:
        # validate password of user
        if use_regular_expression(regex_pattern_to_check_password, signup_password):
            correct_password = True
            print("Valid Password!")
        else:
            error_msg_form.invalid_signup_password = True
            correct_password = False
            print("Invalid Password!")

        # validate confirm password
        if use_regular_expression(regex_pattern_to_check_password, signup_confirm_password):
            correct_confirm_password = True
            print("Valid confirm Password!")
        else:
            correct_confirm_password = False
            print("Invalid confirm Password!")

        # compare both passwords
        if signup_password == signup_confirm_password:
            correct_both_password = True
        else:
            error_msg_form.invalid_signup_confirm_password = True
            correct_both_password = False


    if correct_name and correct_email and correct_password and correct_confirm_password and correct_both_password:
        info_html.login_button_name = signup_name_user
        return render(request, 'otp_verification_page.html')
    else:
        return render(request, 'login_signup_form.html', {'info_html':info_html, 'error_msg_form':error_msg_form})


def otp_verification(request):
    return render(request, 'index.html', {'info_html':info_html})


def forgot_password(request):
    return render(request, 'forgot_password.html')


def reset_password(request):
    return render(request, 'index.html', {'info_html':info_html})


def new_feature_1(request):
    return render(request, 'pankaj_1.html')


def f2(request):
    return render(request, 'pankaj_2.html')


def f3(request):
    return render(request, 'pankaj_3.html')


def f4(request):
    return render(request, 'pankaj_4.html')


def f5(request):
    return render(request, 'pankaj_5.html')


 

