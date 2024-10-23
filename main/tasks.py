from django.core.mail import EmailMultiAlternatives
from celery import shared_task

@shared_task
def tasks_create_review(
    created,
    user_target_email, 
    user_target_username, 
    instance_user_username, 
    instance_text,
    instance_category_type,
    ):
    # instance: id, user_id, text, advert_id, category_type

    print('AAA'*100)
    if not created and instance_category_type == 'AT': 
        print('AT')

        subject = f'Ваш отклик был одобрен!'
        text_content = (
            f'Здравствуйте, {instance_user_username}!\nВаш отклик был рассмотррен пользователем {user_target_username}\n\n'
            f'Сообщение вашего отклика: {instance_text}\n\n'
            f'Увидеть отклик можно в профиле: http://127.0.0.1:8000/profile/'
        )
        html_content = (
            f'<h3>Здравствуйте, {instance_user_username}!\nВаш отклик был рассмотррен пользователем {user_target_username}</h3>'
            f'<p>Сообщение вашего отклика: {instance_text}</p>'
            f'<hr>'
            f'Увидеть отклик можно в <a href="http://127.0.0.1:8000/profile/">'
            f'профиле</a>'
        )

        msg = EmailMultiAlternatives(subject, text_content, None, [user_target_email])
        msg.attach_alternative(html_content, "text/html")
        msg.send()

    elif instance_category_type == 'RJ':
        print('RJ')

    else:
        print('Отклик')
        subject = f'На вашу просьбу откликнулся {instance_user_username}'
        text_content = (
            f'Здравствуйте, {instance_user_username}!\nНа ваше объявление откликнулся {user_target_username}\n\n'
            f'Сообщение: {instance_text}\n\n'
            f'Увидеть отклик можно в профиле: http://127.0.0.1:8000/profile/'
        )
        html_content = (
            f'<h3>Здравствуйте, {instance_user_username}!\nНа ваше объявление откликнулся {user_target_username}</h3>'
            f'<p>Сообщение: {instance_text}</p>'
            f'<hr>'
            f'Увидеть отклик можно в <a href="http://127.0.0.1:8000/profile/">'
            f'профиле</a>'
        )

        msg = EmailMultiAlternatives(subject, text_content, None, [user_target_email])
        msg.attach_alternative(html_content, "text/html")
        msg.send()