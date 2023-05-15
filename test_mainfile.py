import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from test_practice2.Base import Base
from test_practice2.test_consultation import Consultation
from test_practice2.testcase2 import Patient
from test_practice2.testcases import Login


class Test_main(Base):


    def test_login(self):
        obj1 = Login(self.Driver)
        # obj2 = Patient(self.Driver)
        # obj3 = Consultation(self.Driver)



        obj1.loginemail().send_keys("jacobj@gmail.com")
        obj1.enter_pawd().send_keys('Intelspine@123')

        obj1.click_to_login().click()
        time.sleep(2)



    def test_patient(self):
        obj2 = Patient(self.Driver)

        list = obj2.side_bar()
        for lists in list:
            if lists.text == "Patients":
                lists.click()

        time.sleep(2)
        obj2.add_patient().click()
        time.sleep(2)

        obj2.add_patient_titile().select_by_index(1)

        obj2.fill_name().send_keys("Shane")
        obj2.fill_lastname().send_keys("Kalvin")

        obj2.patient_DOB().send_keys('03/02/2023')
        obj2.patient_gender().select_by_index(2)

        obj2.mobile_number().send_keys("78945156464")
        obj2.patient_email().send_keys("shane@gmail.com")

        obj2.patient_address().send_keys('noida')
        obj2.patient_address_zip().send_keys('451565')
        obj2.patient_address_city().send_keys('Bharat')

        obj2.save_button().click()

        self.Driver.refresh() #need to refresh the page because previousely it has oponed the patient window, so focus of the pae is diverted that is why.
        obj2.start_consultation().click()
        time.sleep(2)


    def test_consultation(self):
        obj3 = Consultation(self.Driver)

        obj3.symptom_dropdown().click()
        Selection = obj3.select_dropdownoption()
        for selection in Selection:
            if selection.text == 'Migraine':
                selection.click()
                break


        Radios = obj3.radio_button()
        for radio in Radios:
            if radio.get_attribute('id') == 'sym-lt':
                radio.click()
                break

        obj3.radiator_clicker().click()
        time.sleep(2)

        Radiators = obj3.cons_radiator()
        for radiator in Radiators:
            if radiator.text == 'Upper Arm':
                radiator.click()
                break

        obj3.description_symptoms().click()
        time.sleep(2)

        options = obj3.descrpton_option()
        for option in options:
            if option.text == "sore":
                option.click()
                break

        obj3.input_ago().send_keys('5')

        obj3.ago().select_by_index(2)
        obj3.input_ago2().send_keys('6')

        obj3.ago2().select_by_index(3)

        obj3.onset_click().click()
        time.sleep(2)

        options2 = obj3.on_set()
        for option2 in options2:
            if option2.text == 'Accident':
                option2.click()
                break

        obj3.description_of_injury().send_keys('Patient hit by a car')

        obj3.palliative().click()
        time.sleep(2)

        options3 = obj3.palliativeoptions()
        for option3 in options3:
            if option3.text == 'Sports':
                option3.click()
                break

        obj3.provocative_click().click()
        time.sleep(2)

        provoptions = obj3.provocative_option()
        for provoption in provoptions:
            if provoption.text == "Sports":
                provoption.click()
                break











