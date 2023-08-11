import allure
from models.user import User
from qa_guru_lesson_13.pages.registration_pages import RegistrationPage
from qa_guru_lesson_13.resource import first_name, last_name, user_email


@allure.title("Successful fill form")
def test_registration_user(browser_management):
    registration_page = RegistrationPage()

    test_user = User(
        first_name=first_name,
        last_name=last_name,
        email=user_email,
        gender='Male',
        phone_number='98787675641',
        date_of_birth=('08', 'May', '1996'),
        subjects='Maths',
        hobbies='Sports',
        picture='Cat.jpeg',
        current_address='996 William Rapid, New Gregoryton, UT 78395',
        state='Uttar Pradesh',
        city='Lucknow'
    )

    with allure.step("Open browser"):
        registration_page.open_page()

    with allure.step("Fill form"):
        registration_page.register_user(test_user)

    with allure.step("Check results"):
        registration_page.sshould_have_registered(test_user)
