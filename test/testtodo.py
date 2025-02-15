from selene import browser, have, be


def test_form():
    browser.open('/automation-practice-form')

    browser.element('#firstName').type('Alina')
    browser.element('#lastName').type('Oga')
    browser.element('#userEmail').type('alina.oga@alina.oga')
    browser.element('[for="gender-radio-2"]').click()
    browser.element('#userNumber').type('8800353535')

    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').click().element(
        'option[value="8"]'
    ).click()
    browser.element('.react-datepicker__year-select').click().element(
        'option[value="1999"]'
    ).click()
    browser.element('.react-datepicker__day--026').click()

    browser.element('#subjectsInput').type('Computer Science').press_enter()
    browser.element('[for="hobbies-checkbox-3"]').click()

    browser.element('#currentAddress').type('Abaya 26A')
    browser.element('#state').click().element(
        'div[id^="react-select-3-option"]'
    ).click()
    browser.element('#city').click().element('div[id^="react-select-4-option"]').click()

    browser.element('#submit').press_enter()
    browser.element('.modal-content').should(be.visible)
    browser.element('.table').should(have.text('Alina Oga'))
    browser.element('.table').should(have.text('alina.oga@alina.oga'))
    browser.element('.table').should(have.text('Female'))
    browser.element('.table').should(have.text('8800353535'))
    browser.element('.table').should(have.text('26 September,1999'))
    browser.element('.table').should(have.text('Computer Science'))
    browser.element('.table').should(have.text('Music'))
    browser.element('.table').should(have.text('Abaya 26A'))
    browser.element('.table').should(have.text('NCR Delhi'))
