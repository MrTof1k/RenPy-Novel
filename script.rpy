init python:
    risk_choice = False
    safe_choice = False
    wait_choice = False
    player_gender = "male"
    player_name = "Артём"
    player_call = "artem_call"  # спрайт для разговора по телефону
    player_think = "artem_think"  # спрайт "думает"
    player_crying = "artem_crying" # спрайт "плачет"
    player_document = "artem_document" # спрайт "проверяет документы"
    player_agency = "artem_agency" # спрайт "стоит растроенный у агенства"
    player_perplexity = "artem_perplexity" # спрайт "недоумение героев в варианте С"


# Трансформации
transform pos_far_left_active:
    xalign 0.10
    yalign 1.5
    yoffset -10
    alpha 1.0
    zoom 1.0

transform pos_far_left_inactive:
    xalign 0.10
    yalign 1.2
    yoffset -10
    alpha 0.6
    zoom 0.95

transform pos_far_right_active:
    xalign 0.90
    yalign 1.5
    yoffset -10
    alpha 1.0
    zoom 1.0

transform pos_far_right_inactive:
    xalign 0.90
    yalign 1.2
    yoffset -10
    alpha 0.6
    zoom 0.95


init:
    # Импорт спрайтов

    # Спрайты Артёма
    image artem_call = "Images/artem_call.png"
    image artem_think = "Images/artem_think.png"
    image artem_crying = "Images/artem_crying.png"
    image artem_document = "Images/artem_document.png"
    image artem_agency = "Images/artem_agency.png"
    image artem_perplexity = "Images/artem_perplexity.png"

    # Спрайты Элин
    image elin_call = "Images/elin_call.png"
    image elin_think = "Images/elin_think.png"
    image elin_crying = "Images/elin_crying.png"
    image elin_document = "Images/elin_document.png"
    image elin_agency = "Images/elin_agency.png"
    image elin_perplexity = "Images/elin_perplexity.png"

    # другие спрайты 
    image test_image = "gui/test.jpg" # фон для теста
    image ashot = "Images/ashot.png"
    image room = "Images/room.png"  # общая комната
    image agency = "Images/Real Estate Agency.png"


    # Персонажи
    define a = Character('[player_name]', color="#c8ffc8")
    define seller = Character('Ашот', color="#8d2b2b")


# ========================================
# ТОЧКА ВХОДА
# ========================================
label start:
    
    # Показываем экран выбора персонажа
    call screen character_select
    
    # После выбора переходим к выбору истории
    # call screen chapter_select
    return



# ========================================
# ЭКРАН ВЫБОРА ПЕРСОНАЖА
# ========================================
screen character_select:
    tag menu
    
    # Фон экрана 
    add "gui/select_bg.jpg"
    
    # Заголовок
    text "Выберите персонажа" size 40 xalign 0.5 yalign 0.2 color "#ffffff"
    
    # Кнопки с изображениями
    hbox:
        xalign 0.5
        yalign 0.5
        yoffset 100
        spacing 370
        
        # Артём
        imagebutton:
            idle Transform("gui/artem.png", alpha=0.7)  # Полупрозрачный в покое
            hover "gui/artem.png"  # Полностью видимый при наведении
            action [
                SetVariable("player_gender", "male"),
                SetVariable("player_name", "Артём"),
                SetVariable("player_call", "artem_call"),
                SetVariable("player_think", "artem_think"),
                SetVariable("player_crying", "artem_crying"),
                SetVariable("player_document", "artem_document"),
                SetVariable("player_agency", "artem_agency"),
                SetVariable("player_perplexity", "artem_perplexity"),
                ShowMenu("chapter_select")
            ]
        
        # Элин
        imagebutton:
            idle Transform("gui/elin.png", alpha=0.7)
            hover "gui/elin.png"
            
            action [
                SetVariable("player_gender", "female"),
                SetVariable("player_name", "Элин"),
                SetVariable("player_call", "elin_call"),
                SetVariable("player_think", "elin_think"),
                SetVariable("player_crying", "elin_crying"),
                SetVariable("player_document", "elin_document"),
                SetVariable("player_agency", "elin_agency"),
                SetVariable("player_perplexity", "elin_perplexity"),
                ShowMenu("chapter_select")
            ]
    
    # Кнопка "Назад"
    textbutton "Назад":
        action MainMenu()
        xalign 0.5
        yalign 0.95
        text_size 40
        text_color "#ffffff"
        text_hover_color '#15bb91'

# ========================================
# Выбор главы
# ========================================
screen chapter_select():
    tag menu
    add "gui/main_chapter.jpg"
    
    vbox:
        xalign 0.5
        yalign 0.5
        spacing 20
        textbutton "Глава 1" action Start("story_kv"):
            style "chapter_button"
            text_style "my_chapter_select_button"

        textbutton "Глава 2" action Start("story_car"):
            style "chapter_button"
            text_style "my_chapter_select_button"

        textbutton "Глава 3" action Start("story_job"):
            style "chapter_button"
            text_style "my_chapter_select_button"

    vbox:
        xalign 0.5
        yalign 0.95

        textbutton "Назад" action ShowMenu("character_select"):
            style "chapter_button"
            text_style "my_chapter_select_button"

# ========================================
# ОСНОВНАЯ ИСТОРИЯ Главы 1 (квартира)
# ========================================
label story_kv:
    # Обновляем персонажа с выбранным именем
    $ a = Character(player_name, color="#c8ffc8")
    
    # Показываем спрайт "думает" в зависимости от выбора
    show expression player_think
    a "Как же сложно выбирать квартиры"
    a "Ещё и продавцы долго отвечают..."
    "Звонок… (Звонок телефона, [player_name] хватает аппарат)"
    hide expression player_think with dissolve

    # Показываем общую комнату
    scene room with fade
    
    # Показываем спрайты (динамически в зависимости от выбора)
    show expression player_call at pos_far_right_inactive
    show ashot at pos_far_left_inactive

    # Диалог с Ашотом
    show ashot at pos_far_left_active with dissolve
    seller "[player_name]? Это насчёт квартиры на Таганке! Ситуация горит — только что звонили два покупателя..."

    show expression player_call at pos_far_right_active with dissolve
    show ashot at pos_far_left_inactive with dissolve
    a "Откуда вы знаете моё имя? Я только просмотрел объявление..."

    show ashot at pos_far_left_active with dissolve
    show expression player_call at pos_far_right_inactive with dissolve
    seller "Да риелтор передал! Не суть. Слушай, я в разводе — бывшая требует денег к утру. Задаток 50 тысяч — и квартира твоя!"
    
    show expression player_call at pos_far_right_active with dissolve
    show ashot at pos_far_left_inactive with dissolve
    a "А документы можно посмотреть сначала?"
    
    show ashot at pos_far_left_active with dissolve
    show expression player_call at pos_far_right_inactive with dissolve
    seller "Документы?! Да я их завтра привезу! Ты что, не понимаешь — через час эта цена уйдёт?!"
    
    show expression player_call at pos_far_right_active with dissolve
    show ashot at pos_far_left_inactive with dissolve

    # ВЫБОР
    menu:
        "Что ответить?"

        "Хорошо, говорите реквизиты. Перевожу 50 000 ₽":
            $ risk_choice = True
            jump choice_a
        
        "Без сканов паспорта и выписки ЕГРН я ничего не перевожу":
            $ safe_choice = True
            jump choice_b

        "Давайте я думаю до утра. Без задатка":
            $ wait_choice = True
            jump choice_c


# ========================================
# ФИНАЛЫ для глава 1 (квартира)
# ========================================
label choice_a:
    
    scene room with fade
    show ashot at pos_far_left_active
    show expression player_call at pos_far_right_active
    
    a "Хорошо, говорите реквизиты. Перевожу 50 000 ₽"
    seller "Отлично! Вот номер карты: 5555 6666 7777 8888..."
    
    show expression player_crying with fade
    hide room
    hide ashot
    hide exit_transition player_call
    
    
    "Через час я понимаю... Ашот заблокировал мой номер."
    "50 000 рублей исчезли. Квартира оказалась мошенничеством."
    return


label choice_b:
    scene room with fade
    show ashot at pos_far_left_active
    show expression player_call at pos_far_right_active
    
    a "Без сканов паспорта и выписки ЕГРН я ничего не перевожу"
    seller "Ты серьёзно? Ну ладно... Щас скину документы."
    
    hide room
    hide ashot
    hide exit_transition player_call
    show expression player_document
    "Через 10 минут приходят сканы. Всё выглядит легально."
    "Я договариваюсь о встрече завтра в офисе агентства."
    jump next_scene_agency


label choice_c:
    scene room with fade
    show ashot at pos_far_left_inactive with dissolve
    show expression player_call at pos_far_right_active
    a "Давайте я думаю до утра. Без задатка"

    show ashot at pos_far_left_active with dissolve
    show expression player_call at pos_far_right_inactive with dissolve
    seller "Как хочешь... Но завтра цена будет выше!"

    scene room with fade
    
    show expression player_perplexity

    

    "На следующее утро я перезваниваю Ашоту..."
    "Номер недоступен. Объявление о квартире удалено."
    
    "Деньги в сохранности, но упущена возможность?"
    return



label next_scene_agency:
    scene agency with fade
    show expression player_agency at pos_far_right_active
    "Придя на место [player_name] лицезреет заброшенное агентство"
    a "Нужно найти другого риелтора..."
    return

# ========================================
# ОСНОВНАЯ ИСТОРИЯ Главы 2 (машины)
# ========================================
label story_car:
    scene test_image
    "Нас плохо кормить, но мы стараться написать история"

# ========================================
# ОСНОВНАЯ ИСТОРИЯ Главы 3 (трудоустройство)
# ========================================
label story_job:
    scene test_image
    "Нас плохо кормить, но мы стараться написать история"
