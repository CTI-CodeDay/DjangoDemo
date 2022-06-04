Some work around have been made in order to follow [this django tutorial](https://www.youtube.com/watch?v=F5mRW0jo-U4)

Web application was created in Django Version 4.0.5 due to not being able to run the application on Django 2.0.7 (from the tutorial)

In addition, a small piece of code has been added to the settings that allows access into the admin component without the Forbiden 403 Error. Shown below. [Reference (first solution)](https://dev.to/shriekdj/unable-to-login-django-admin-after-update-giving-error-forbidden-403-csrf-verification-failed-request-aborted-36g9)

```
CSRF_TRUSTED_ORIGINS = ['http://*', 'https://*', 'https://masonjason23-djangodemo-v6gpgvx9phwwv4-8000.githubpreview.dev/*']
```