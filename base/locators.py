from selenium.webdriver.common.by import By

class Links(object):
    BUYME_LINK = "https://buyme.co.il/"
    
class BuyMeLocators(object):
    SIGN_BUTTON = (By.CSS_SELECTOR, "a[aria-label='כניסה / הרשמה']")
    # TOSIGN_BUTTON = (By.XPATH, "span[text()='להרשמה']")
    TOSIGN_BUTTON = (By.CSS_SELECTOR, "span[aria-label='להרשמה']")
    NAME_INPUT = (By.CSS_SELECTOR, "input[aria-label='שם פרטי']")
    MAIL_INPUT = (By.CSS_SELECTOR, "input[type='email']")
    PASSWORD_INPUT = (By.ID, "valPass")
    VALIDATE_INPUT = (By.CSS_SELECTOR, "input[placeholder='אימות סיסמה']")
    CONFIRM_BOX = (By.CSS_SELECTOR, "div[aria-labelledby='אני מסכימ/ה למדיניות הפרטיות ולתנאי השימוש ב-BUYME שתאסוף עלי מידע לצורך תפעול שוברי המתנה.']")
    SUBMIT_BUTTON = (By.ID, "ember1983")
    POPUP_CLOSE = (By.CSS_SELECTOR, "div[aria-label='סגור חלונית פופ-אפ']")
    POPUP2_CLOSE = (By.CSS_SELECTOR, "button[aria-label='סגור פופ-אפ']")
    POPUP3_CLOSE = (By.CSS_SELECTOR, "button[aria-label='כפתור סגירה']")
    # PASSWORD_ERROR = (By.XPATH, "//li[text()='הסיסמאות לא זהות, אולי זה מהתרגשות :)']")
    VALIDATION_ERROR = (By.ID, "parsley-id-27")
    EMAIL_ERROR = (By.ID, "parsley-id-23")
    LOG_EMAIL_INPUT = (By.ID, "ember1923")
    LOG_PASSWORD_INPUT = (By.ID, "ember1930")
    # CONFIRM_ERROR = (By.CLASS_NAME, "register-error")
    # LOG_BUTTON = (By.ID, "ember2007")
    LOG_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    ACOUNT_BUTTON = (By.XPATH, "//span[text()='החשבון שלי']")
    LOG_PASSWORD_ERROR = (By.XPATH, "//div[text()='אחד או יותר מהפרטים שהזנת אינם נכונים.']")
    LOG_EMAIL_ERROR = (By.XPATH, "//li[text()='ערך זה צריך להיות כתובת אימייל.']")
    AMOUNT_LIST = (By.CSS_SELECTOR, "span[title='סכום']")
    def find_option(value):
        return (By.XPATH, f"//span[contains(text(), '{value}')]")
    REGION_LIST = (By.CSS_SELECTOR, "span[title='אזור']")
    CATEGORY_LIST = (By.CSS_SELECTOR, "span[title='קטגוריה']")
    # SEARCH_BUTTON = (By.ID, "ember3079")
    SEARCH_BUTTON = (By.XPATH, "//a[text()='תמצאו לי מתנה']")
    # RESULTS_GRID = (By.CLASS_NAME, "grid bm-product-cards")
    RESULTS_GRID = (By.CSS_SELECTOR, "ul[class='grid bm-product-cards']")
    # RESULT_CARD = ((By.CLASS_NAME, "ember-view bm-product-card-link mx-4 lr-6 sm-12"))
    RESULT_CARD = (By.CSS_SELECTOR, "div[class='ember-view bm-product-card-link mx-4 lr-6 sm-12']")
    CARD_NAME = (By.CSS_SELECTOR, 'span[class="name bm-subtitle-1"]')
    GIFT_GRID = (By.CSS_SELECTOR, 'ul[class="grid gifts-list"]')
    GIFT_CARD = (By.CSS_SELECTOR, 'li[class="ember-view bm-gift-card-link"]')
    GIFT_SELECT = (By.XPATH, 'span[text()="בחירה"]')
    RECIEVER_NAME = (By.CSS_SELECTOR, 'input[aria-label="שם מקבל המתנה. כדי לשלוח את המתנה אליך. נווט אחורה ושנה את הבחירה בכפתורי הרדיו"]')
    RECIEVER_MESSAGE = (By.CSS_SELECTOR, 'textarea[placeholder="מזל טוב, תודה רבה או פשוט מלא אהבה? כאן כותבים מילים טובות ואיחולים שמחים"]')
    SEND_BUTTON = (By.CSS_SELECTOR, 'button[class="ember-view bm-btn no-reverse main xl stretch"]')
    SENDING_GRID = (By.CSS_SELECTOR, 'div[class="ember-view bm-sending-methods"]')
    SEND_OPTION = (By.CSS_SELECTOR, 'div[role="checkbox"]')
    RECIEVER_PHONE = (By.ID, "sms")
    RECIEVER_MAIL = (By.ID, "email")
    SENDER_NAME = (By.CSS_SELECTOR, 'input[placeholder="שם שולח המתנה"]')
    SENDER_PHONE = (By.CSS_SELECTOR, 'input[placeholder="מספר נייד"]')