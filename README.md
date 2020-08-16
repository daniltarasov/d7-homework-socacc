# d7-homework

1. Из папки с джанго (c активированным вирт. окружением) выполнить: git clone https://github.com/daniltarasov/d7-homework-socacc.git
2. cd d7-homework-socacc
3. pip install -r requirements.txt
4. python manage.py runserver

Это проект с реализацией профиля для SocialAccaunt через расширение SocialAccount.
Минус этого подхода - сохраненные в extra_data данные стираются при следующем заходе.
Не стираются в проекте https://github.com/daniltarasov/d7-homework-usermodel


Залогиниться через Github: Вход -> "Github"

Пароль админа: admin-admin

По непонятной причине иногда при авторизации через гитхаб создается пользователь с именем "user" вместо гитхабовского. 
Это какой-то глюк allautha, я здесь непричем. Нужно зайти в админку, удалить этот socialaccount и связанного с ним юзера в папке users, 
разлогиниться из гитхаба, перезапустить браузер, может еще и джанго.

