Selenium Automation:

Python script test.py uses Selenium to automate form filling.
The script navigates to the form URL, fills in specified fields programmatically.
To use it you need to change the find_element attribute according to need
While filling the data just change values in send_keys()

Screenshot Capture:

After successful form submission, Selenium captures a screenshot of the filled form page.
The screenshot is saved to location defined by driver.save_screenshot(r"PATH_TO_SAVE_SCREENSHOT")
If some things don't work accordingly due to poor internet connection change time.sleep()
To fill the form run `python manage.py test`

Email Integration with Django:

Django's email functionality is leveraged to send the captured screenshot via email.
Ensured that Django settings are configured with appropriate SMTP settings for email delivery.
To Reuse the code just replace the corresponding variables in .env.example and rename it as .env
