import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class Patient:
    def __init__(self, Driver):
        self.Driver = Driver

    sidebaar = (By.CSS_SELECTOR, 'li[class="nav-item"] a ')
    addpatient = (By.CSS_SELECTOR, "a[class='btn btn-primary']")
    addpatienttittle = (By.NAME, "salutation")
    filename = (By.CSS_SELECTOR, "#fname")
    filelastname = (By.CSS_SELECTOR, "#lname")
    mobilenumber = (By.CSS_SELECTOR, "input[id='Email/mobileNumber']")
    patientemail = (By.CSS_SELECTOR, '#email')
    patientaddress = (By.XPATH, '(//input[@id="fullAddress"])[1]')
    patientaddresszip = (By.XPATH, '(//input[@id="fullAddress"])[2]')
    patientaddresscity = (By.XPATH, '(//input[@id="fullAddress"])[3]')
    patientgender = (By.NAME, 'gender')
    patientDOB = (By.CSS_SELECTOR, '#DOB')
    savebutton = (By.CSS_SELECTOR, "button[class='btn btn-primary w-sm-40']")
    startconsultation = (By.XPATH, "(//a[@title='Edit'])[1]")


    def side_bar(self):
        return self.Driver.find_elements(*Patient.sidebaar)

    def add_patient(self):
        return self.Driver.find_element(*Patient.addpatient)

    def add_patient_titile(self):
        return Select(self.Driver.find_element(*Patient.addpatienttittle))

    def fill_name(self):
        return self.Driver.find_element(*Patient.filename)

    def fill_lastname(self):
        return self.Driver.find_element(*Patient.filelastname)

    def mobile_number(self):
        return self.Driver.find_element(*Patient.mobilenumber)

    def patient_email(self):
        return self.Driver.find_element(*Patient.patientemail)

    def patient_address(self):
       return  self.Driver.find_element(*Patient.patientaddress)

    def patient_address_zip(self):
        return self.Driver.find_element(*Patient.patientaddresszip)

    def patient_address_city(self):
        return self.Driver.find_element(*Patient.patientaddresscity)

    def patient_gender(self):
        return Select(self.Driver.find_element(*Patient.patientgender))

    def patient_DOB(self):
        return self.Driver.find_element(*Patient.patientDOB)

    def save_button(self):
        return self.Driver.find_element(*Patient.savebutton)

    def start_consultation(self):
        return self.Driver.find_element(*Patient.startconsultation)











