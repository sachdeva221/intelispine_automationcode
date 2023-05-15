from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class Consultation:
    def __init__(self, Driver):
        self.Driver = Driver

    dropdown1 = (By.XPATH, "(//div[@class=' css-1wy0on6'])[1]")
    selectdropdownoption = (By.CSS_SELECTOR, 'div[class=" css-10wo9uf-option"]')
    radiobutton = (By.XPATH, '(//div[@class="row mt-4"])[1]/div/input')
    radiatorclick = (By.XPATH, '(//div[@class=" css-13cymwt-control"])[2]')
    radiate = (By.CSS_SELECTOR, 'div[class=" css-10wo9uf-option"]')
    descriptionsymptoms = (By.XPATH, "(//div[@class=' css-hlgwow'])[3]")
    descriptionsymptomsoption = (By.XPATH, "(//div[@class=' css-10wo9uf-option'])")
    inputnumber = (By.XPATH, '(//input[@class="form-control mt-1"])[1]')
    agos = (By.NAME, 'ago')
    inputnumber2 = (By.XPATH, '(//input[@class="form-control mt-1"])[2]')
    agos2 = (By.NAME, 'duration')
    onsetclick = (By.XPATH, '(//div[@class=" css-19bb58m"])[4]')
    onsetopion = (By.CSS_SELECTOR, 'div[aria-disabled="false"]')
    descriptionofinjury = (By.NAME, 'describeInjury')
    Palliativeclick = (By.XPATH, '(//div[@class=" css-19bb58m"])[5]')
    palliaiveoptions = (By.CSS_SELECTOR, 'div[aria-disabled="false"]')
    provocative = (By.XPATH, '(//div[@class=" css-19bb58m"])[6]')
    provcativeoption = (By.CSS_SELECTOR, 'div[aria-disabled="false"]')
    warning = (By.CSS_SELECTOR, 'div[class=" css-t3ipsp-control"]')




    def symptom_dropdown(self):
        return self.Driver.find_element(*Consultation.dropdown1)

    def select_dropdownoption(self):
        return self.Driver.find_elements(*Consultation.selectdropdownoption)


    def radio_button(self):
        return self.Driver.find_elements(*Consultation.radiobutton)

    def radiator_clicker(self):
        return self.Driver.find_element(*Consultation.radiatorclick)

    def cons_radiator(self):
        return self.Driver.find_elements(*Consultation.radiate)

    def description_symptoms(self):
        return self.Driver.find_element(*Consultation.descriptionsymptoms)

    def descrpton_option(self):
        return self.Driver.find_elements(*Consultation.descriptionsymptomsoption)

    def ago(self):
        return Select(self.Driver.find_element(*Consultation.agos))

    def input_ago(self):
        return self.Driver.find_element(*Consultation.inputnumber)

    def input_ago2(self):
        return self.Driver.find_element(*Consultation.inputnumber2)

    def ago2(self):
        return Select(self.Driver.find_element(*Consultation.agos2))

    def onset_click(self):
        return self.Driver.find_element(*Consultation.onsetclick)

    def on_set(self):
        return self.Driver.find_elements(*Consultation.onsetopion)

    def description_of_injury(self):
        return self.Driver.find_element(*Consultation.descriptionofinjury)

    def palliative(self):
        return self.Driver.find_element(*Consultation.Palliativeclick)

    def palliativeoptions(self):
        return self.Driver.find_elements(*Consultation.palliaiveoptions)

    def provocative_click(self):
        return self.Driver.find_element(*Consultation.provocative)

    def provocative_option(self):
        return self.Driver.find_elements(*Consultation.provcativeoption)

