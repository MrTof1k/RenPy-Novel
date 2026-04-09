init python:
    config.game_menu_action = ShowMenu("pause_menu")
    #Отладка достижений
    # persistent.unlocked_achievements = []
    # renpy.save_persistent()
    # renpy.notify("Достижения сброшены.")

    risk_choice = False
    safe_choice = False
    wait_choice = False
    lawyer_hire = False

    mfc_choice = False
    mfc_choice_index = 0
    bank_choice = False
    bank_choice_index = 0
    realtor_choice = False
    realtor_choice_index = 0
    lawyer_choice = False
    yk_choice = False

    player_gender = "male"
    player_name = "Артём"
    player_call = "artem_call"  # спрайт для разговора по телефону
    player_think = "artem_think"  # спрайт "думает"
    player_strit = "artem_strit" # спрайт идёт по улице
    player_document = "artem_document" # спрайт "проверяет документы"
    player_robbery = "artem_robbery" # спрайт пойман на воровстве
    player_perplexity = "artem_perplexity" # спрайт "недоумение героев"
    player_backpack = "artem_backpack" #спрайт герой с рюкзаком
    player_prison = "artem_prison" #спрайт персонаж за решоткой
    player_interested = "artem_interested" #спрайт заинтерисованный артём
    player_maney = "artem_maney" #Спрайт протягивает деньги
    player_receipt = "artem_receipt"
    player_agency = "artem_agency"
    player_crying = "artem_crying"
    player_mfc = "artem_mfc"
    player_mfc_tiket = "artem_mfc_tiket"
    player_mfc_window = "artem_mfc_window"
    player_backpack_doc = "artem_backpack_doc"

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

transform highlight:
    # Немного увеличиваем и добавляем свечение
    linear 0.1 zoom 1.1
    matrixcolor BrightnessMatrix(0.2)  # делаем ярче

transform normal:
    linear 0.1 zoom 1.0
    matrixcolor BrightnessMatrix(0.0)

init:
    # Импорт спрайтов

    # Спрайты Артёма
    image artem_backpack = "Images/artem_character/artem_backpack.png" #Артём с рюкзаком
    image artem_backpack_doc = "Images/artem_character/artem_backpack_doc.png" #Артём с рюкзаком и документами
    image artem_perplexity = "Images/artem_character/artem_perplexity.png"
    image artem_interested = "Images/artem_character/artem_interested.png"
    image artem_agency = "Images/artem_character/artem_agency.png"
    image artem_call = "Images/artem_character/artem_call.png"
    image artem_maney = "Images/artem_character/artem_maney.png" #Протягивает деньги
    image artem_robbery = "Images/artem_scene/artem_robbery.png" #Пойман при грабедже
    image artem_prison = "Images/artem_scene/artem_prison_img.png" #За решёткой
    image artem_strit = "Images/artem_scene/artem_strit.png" #Артём на улице
    image artem_think = "Images/artem_scene/artem_think.png" #Артём думает
    image artem_receipt = "Images/artem_scene/artem_receipt.png"
    image artem_crying = "Images/artem_scene/artem_crying.png"
    image artem_mfc = "Images/artem_scene/artem_mfc.png"
    image artem_mfc_tiket = "Images/artem_scene/artem_mfc_tiket.png"
    image artem_mfc_window = "Images/artem_scene/artem_mfc_window.png"

    # Спрайты Элин
    image elin_backpack = "Images/elin_character/elin_backpack.png" #Элин с рюкзаком
    image elin_backpack_doc = "Images/elin_character/elin_backpack_doc.png" #Элин с рюкзаком и документами
    image elin_perplexity = "Images/elin_character/elin_perplexity.png" #Элин в недоумении
    image elin_interested = "Images/elin_character/elin_interested.png"
    image elin_agency = "Images/elin_character/elin_agency.png"
    image elin_call = "Images/elin_character/elin_call.png"
    image elin_maney = "Images/elin_character/elin_maney.png" #Протягивает деньги
    image elin_robbery = "Images/elin_scene/elin_robbery.png" #Поймана при грабедже
    image elin_prison = "Images/elin_scene/elin_prison_img.png" #За решёткой
    image elin_strit = "Images/elin_scene/elin_strit.png" #Элин на улице
    image elin_think = "Images/elin_scene/elin_think.png" #Элин думает
    image elin_receipt = "Images/elin_scene/elin_receipt.png"
    image elin_crying = "Images/elin_scene/elin_crying.png"
    image elin_mfc = "Images/elin_scene/elin_mfc.png"
    image elin_mfc_tiket = "Images/elin_scene/elin_mfc_tiket.png"
    image elin_mfc_window = "Images/elin_scene/elin_mfc_window.png"

    # Спрайты риелтора
    image realtor_interior_image = "Images/realtor/realtor interior image.png" #офис
    image realtor_dmitriy = "Images/realtor/realtor dmitriy.png" #Дмитрий стоя с блокнотом
    image realtor_dmitriy_laughter = "Images/realtor/realtor dmitriy laughter.png" #Риелтор смех
    image realtor_dmitriy_display = "Images/realtor/realtor dmitriy display.png" #Риелтор показывает блокнот
    image realtor_dmitriy_surprised = "Images/realtor/realtor dmitriy surprise.png" #Удивление риелтора
    image realtor_dmitriy_upset = "Images/realtor/realtor dmitriy upset.png" #Расстроенный 
    image realtor_dmitriy_record = "Images/realtor/realtor dmiriy record.png" #Риелтор пишет
    image realtor_bilding_image = "Images/realtor/realtor bilding image.png"
    image realtor_dmitriy_call = "Images/realtor/realtor dmitriy call.png"
    

    #Спрайты мфц
    image mfc_holl = "Images/mfc/mfc_holl.png"

    #Спрайты нотариюса/юриста
    image notary_bilding_interior = "Images/notary/notary_bilding_interior.png"
    image notary_bilding = "Images/notary/notary_bilding.png"
    image lawyer_character = "Images/notary/lawyer_character.png"

    # Спрайты банка
    image bank_scene_image = "Images/bank_scene/bank_scene.png" #фон банка
    image bank_specialist = "Images/bank_scene/bank_specialist.png" #специалист банка
    image bank_specialist_writes = "Images/bank_scene/bank_specialist_writes.png" #специалист банка записывает
    image bank_specialist_surprised = "Images/bank_scene/bank_specialist_surprised.png" #Удивлённый банкир
    image contracts = "Images/bank_scene/contracts.png"

    # другие спрайты 
    image test_image = "gui/test.jpg" # фон для теста

    #Спрайты продавца
    image seller_character = "Images/seller/seller_character.png"


    #Спрайты карты
    image city_map = "Images/map/city map.png" #фон карта 
    image mfc_building = "Images/map/mfc.png" #здание мфц
    image lawyer_building = "Images/map/lawyer.png" #здание юриста
    image realtor_building = "Images/map/realtor.png" #здание риелтора
    image bank_building = "Images/map/bank.png" #здание банка
    image yk_building = "Images/map/yk.png" #здание ук
    

    # Персонажи
    define player = Character('[player_name]', color="#c8ffc8")
    default character_realtor = Character('Дмитрий', color = "#57ad4c")
    default bankir = Character('Специалист банка: ', color = "#57ad4c")
    default mfc = Character('Сотрудник МФЦ', color = "#57ad4c")
    default notary = Character('Нотариус', color = "#57ad4c")
    default lawyer = Character('Юрист', color = "#57ad4c")
    default seller = Character('Продавец', color = "#57ad4c")
    
# ========================================
# ТОЧКА ВХОДА
# ========================================
label start:
    
    # Показываем экран выбора персонажа
    call screen character_select
    
    
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
                SetVariable("player_think", "artem_think"),
                SetVariable("player_robbery", "artem_robbery"),
                SetVariable("player_prison", "artem_prison"),
                SetVariable("player_perplexity", "artem_perplexity"),
                SetVariable("player_backpack", "artem_backpack"),
                SetVariable("player_backpack_doc", "artem_backpack_doc"),
                SetVariable("player_strit", "artem_strit"),
                SetVariable("player_interested", "artem_interested"),
                SetVariable("player_maney", "artem_maney"),
                SetVariable("player_receipt", "artem_receipt"),
                SetVariable("player_agency", "artem_agency"),
                SetVariable("player_call", "artem_call"),
                SetVariable("player_crying", "artem_crying"),
                SetVariable("player_mfc", "artem_mfc"),
                SetVariable("player_mfc_tiket", "artem_mfc_tiket"),
                SetVariable("player_mfc_window", "artem_mfc_window"),
                ShowMenu("chapter_select")
            ]
        
        # Элин
        imagebutton:
            idle Transform("gui/elin.png", alpha=0.7)
            hover "gui/elin.png"
            
            action [
                SetVariable("player_gender", "female"),
                SetVariable("player_name", "Элин"),
                SetVariable("player_think", "elin_think"),
                SetVariable("player_robbery", "elin_robbery"),
                SetVariable("player_prison", "elin_prison"),
                SetVariable("player_perplexity", "elin_perplexity"),
                SetVariable("player_backpack", "elin_backpack"),
                SetVariable("player_backpack_doc", "elin_backpack_doc"),
                SetVariable("player_strit", "elin_strit"),
                SetVariable("player_interested", "elin_interested"),
                SetVariable("player_maney", "elin_maney"),
                SetVariable("player_receipt", "elin_receipt"),
                SetVariable("player_agency", "elin_agency"),
                SetVariable("player_call", "elin_call"),
                SetVariable("player_crying", "elin_crying"),
                SetVariable("player_mfc", "elin_mfc"),
                SetVariable("player_mfc_tiket", "elin_mfc_tiket"),
                SetVariable("player_mfc_window", "elin_mfc_window"),
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

        textbutton "Глава 2" action Start("test_map"):
            style "chapter_button"
            text_style "my_chapter_select_button"

        textbutton "Глава 3" action Start("test_map"):
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
    $ grant_achievement("first_start")
    # Обновляем персонажа с выбранным именем
    $ player = Character(player_name, color="#c8ffc8")
    
    # Показываем спрайт "думает" в зависимости от выбора
    show expression player_think
    "Ты закончил институт, устраиваешься на работу, следующий этап- покупка квартиры."
    "Надо сходить к риелтору!"
    hide expression player_think with dissolve
    $ realtor_choice = True
    jump choice_scene

# ========================================
# Экран для всплывающих подсказок (простой вариант)
# ========================================    
screen simple_icon_tooltip(message, tooltip_x, tooltip_y):
    zorder 100
    
    frame:
        background Solid("#2b2b2be6")
        padding (10, 5)
        xanchor 0.5
        xpos tooltip_x
        ypos tooltip_y
        
        text message:
            color "#ffffff"
            size 18
            xalign 0.5

# ========================================
# Экран с кнопками домов 
# ========================================
screen city_map_screen():
    add "city_map"
    default hovered_button = None

    # Кнопка МФЦ
    imagebutton:
        idle "mfc_building"
        hover "mfc_building"
        pos (0, 410)
        action Return("mfc")
        
        hovered [
            SetScreenVariable("hovered_button", "mfc"),
            # Show("simple_icon_tooltip", 
            #         message="МФЦ", Ы
            #         tooltip_x=430 + 50,  
            #         tooltip_y=150 - 30)  
            ]
        unhovered [
            SetScreenVariable("hovered_button", None),
            Hide("simple_icon_tooltip")
        ]
        
        if hovered_button == "mfc":
            at highlight
        else:
            at normal
    
    # Кнопка Банка
    imagebutton:
        idle "bank_building"
        hover "bank_building"
        pos (50, 112)
        action Return("bank")
        
        hovered [
            SetScreenVariable("hovered_button", "bank"),
            # Show("simple_icon_tooltip", 
            #         message="Банк", 
            #         tooltip_x=400 + 50, 
            #         tooltip_y=250 - 30)
        ]
        unhovered [
            SetScreenVariable("hovered_button", None),
            Hide("simple_icon_tooltip")
        ]
        
        if hovered_button == "bank":
            at highlight
        else:
            at normal
    
    # Кнопка Риелтора
    imagebutton:
        idle "realtor_building"
        hover "realtor_building"
        pos (765, 152)
        action Return("realtor")
        
        hovered [
            SetScreenVariable("hovered_button", "realtor"),
            # Show("simple_icon_tooltip", 
            #         message="Риелтор", 
            #         tooltip_x=600 + 50, 
            #         tooltip_y=350 - 30)
        ]
        unhovered [
            SetScreenVariable("hovered_button", None),
            Hide("simple_icon_tooltip")
        ]
        
        if hovered_button == "realtor":
            at highlight
        else:
            at normal
    
    # Кнопка УК 
    imagebutton:
        idle "yk_building"
        hover "yk_building"
        pos (800, 327)
        action Return("yk")
        
        hovered [
            SetScreenVariable("hovered_button", "yk"),
            # Show("simple_icon_tooltip", 
            #         message="УК", 
            #         tooltip_x=550 + 50, 
            #         tooltip_y=500 - 30)
        ]
        unhovered [
            SetScreenVariable("hovered_button", None),
            Hide("simple_icon_tooltip")
        ]
        
        if hovered_button == "yk":
            at highlight
        else:
            at normal
    
    # Кнопка Юриста
    imagebutton:
        idle "lawyer_building"
        hover "lawyer_building"
        pos (500, 455)
        action Return("lawyer")
        
        hovered [
            SetScreenVariable("hovered_button", "lawyer"),
            # Show("simple_icon_tooltip", 
            #         message="Юрист", 
            #         tooltip_x=350 + 50, 
            #         tooltip_y=450 - 30)
        ]
        unhovered [
            SetScreenVariable("hovered_button", None),
            Hide("simple_icon_tooltip")
        ]
        
        if hovered_button == "lawyer":
            at highlight
        else:
            at normal


# ========================================
# Метка выбора
# ========================================
label choice_scene:
    hide player_think
    scene city_map
    
    while True:
        call screen city_map_screen
        
        if _return == "mfc" and mfc_choice:
            
            jump mfc_scene

        elif _return == "mfc" and not mfc_choice:
            $ renpy.notify("Они щас закрыты на обед")
            $ renpy.pause(0.5)

        elif _return == "bank" and bank_choice:
           
            jump bank_scene

        elif _return == "bank" and not bank_choice:
            $ renpy.notify("Банк сегодня закрыт, приходите в другое время")
            $ renpy.pause(0.5)

        elif _return == "realtor" and realtor_choice:
            if realtor_choice_index == 0:
                jump realtor_scene_0
            elif realtor_choice_index == 1:
                jump realtor_scene_1

        elif _return == "realtor" and not realtor_choice:
            $ renpy.notify("Этот визит ничего не даст. Подумай ещё.")
            $ renpy.pause(0.5)

        elif _return == "lawyer" and lawyer_choice:
           
            jump lawyer_scene

        elif _return == "lawyer" and not lawyer_choice:
            $ renpy.notify("Сейчас юрист тебе не поможет. Попробуй что-то другое.")
            $ renpy.pause(0.5)

        elif _return == "yk":
            $ renpy.notify("Пока рано обращаться в УК.")
            $ renpy.pause(0.5)


label mfc_scene:
    if mfc_choice_index == 0:
        show mfc_holl with fade
        "Раз вы решили продолжить покупку вторичного жилья, нужно убедиться, что продавец действительно имеет право распоряжаться квартирой."

        "Для этого вы предлагаете вместе обратиться за выпиской из ЕГРН."

        "В этом документе вас прежде всего интересует графа «Собственники»."


        show expression player_mfc with fade

        "Спустя несколько минут документ оказывается у вас в руках."

        "Вы внимательно проверяете сведения."

        "Продавец действительно указан как собственник недвижимости."

        "Это хороший знак: теперь формальных препятствий для сделки нет."

        "Вы чувствуете себя спокойнее."

        "Следующий шаг — зарегистрировать дальнейшие действия."

        show expression player_mfc_tiket with fade

        "Вы подходите к терминалу и берёте талон."
        "На табло загорается ваш номер."

        show expression player_mfc_window with fade

        "Вы подходите к окну."

        mfc "Вы уже проверили собственника. Теперь следующий шаг — оформление сделки."

        mfc "Для этого вам потребуется нотариус."

        "Вы немного удивляетесь."

        player "Нотариус? Значит, всё серьёзнее, чем казалось."

        mfc "Да. Нотариус удостоверяет сделку и проверяет документы сторон."

        mfc "Без этого безопасно завершить покупку не получится."

        "Вы киваете и делаете заметку."
        
        $ mfc_choice = False
        $ lawyer_choice = True
        jump choice_scene
    elif mfc_choice_index == 1:
        jump test_map
    
    else:
        jump test_map


   

    
    return

# ========================================
# Сцена в банке с её исходами
# ========================================
label bank_scene:
    if bank_choice_index == 0:
        scene bank_scene_image with fade

        show expression player_backpack as player_sprite at pos_far_left_inactive
        show bank_specialist as bank_specialist at pos_far_right_inactive

        show expression player_backpack as player_sprite at pos_far_left_active with dissolve
        show bank_specialist as bank_specialist at pos_far_right_inactive with dissolve
        player "Здравствуйте! Хочу получить предварительное одобрение на ипотеку для покупки квартиры."

        show bank_specialist as bank_specialist at pos_far_right_active with dissolve
        show expression player_backpack as player_sprite at pos_far_left_inactive with dissolve
        bankir "Добрый день. Рад помочь."
        bankir "Для расчета нам понадобятся данные: ваши паспортные данные, информация о трудоустройстве и официальных доходах за последние 6 месяцев"
        bankir "А также примерная стоимость квартиры и размер первоначального взноса." 
        
        show expression player_backpack as player_sprite at pos_far_left_active with dissolve
        show bank_specialist as bank_specialist at pos_far_right_inactive with dissolve
        menu:
            "Как поступить?"

            "Быстрый, но рискованный вариант":
                jump bank_chice_A

            "Документально-аналитический вариант":
                jump bank_chice_B


        return

    elif bank_choice_index == 1:
        scene bank_scene_image with fade
        show expression player_backpack as player_sprite at pos_far_left_inactive
        show bank_specialist as bank_specialist at pos_far_right_inactive
        "Деньги за квартиру не передаются из рук в руки — это опасно."
        "Самый безопасный способ — расчёт через банковскую ячейку или аккредитив."

        show expression player_backpack as player_sprite at pos_far_left_inactive
        show bank_specialist as bank_specialist at pos_far_right_active
        bankir "Мы подготовили договор аренды ячейки."
        bankir "Ключ будет у вас, второй — у банка. Доступ продавца к деньгам возможен только при предъявлении выписки из ЕГРН с вашим именем как нового собственника."
        bankir "Это прописано здесь, в дополнительном соглашении."

        menu:
            "Проверить договор?"
            "Да, я проверяю этот пункт":
                jump bank_chice_C_1

            "Ладно, я доверяю":
                jump bank_chice_C_2
        
    else:
        jump test_map

label bank_chice_C_1:
    scene contracts with fade
    player "Хорошо, всё зафиксировано. Без регистрации деньги никто не получит."
    $ grant_achievement("financial_security")
    jump bank_chice_D
    
label bank_chice_C_2:
    scene bank_scene_image with fade

    show expression player_backpack as player_sprite at pos_far_left_active with dissolve
    show bank_specialist as bank_specialist at pos_far_right_inactive with dissolve
    player "Наверное, всё стандартно… не буду вникать."

    "Вы не убедились, что доступ продавца ограничен условиями регистрации. Это создаёт риск потери денег."
    jump bank_chice_D   

label bank_chice_D:
    scene bank_scene_image with fade

    show expression player_backpack as player_sprite at pos_far_left_active with dissolve
    show seller_character as seller_character at pos_far_right_inactive with dissolve
    player "И я кладу в ячейку только 90%% суммы."
    player "Оставшиеся 10%% передам продавцу после полной переписки счетов в управляющей компании, как мы и договаривались."

    show expression player_backpack as player_sprite at pos_far_left_inactive with dissolve
    show seller_character as seller_character at pos_far_right_active with dissolve
    seller "Договорились. Так безопасно для всех."

    show expression player_backpack as player_sprite at pos_far_left_inactive
    show bank_specialist as seller_character at pos_far_right_active
    bankir "Отлично. Договор подписан. Срок аренды ячейки — 14 дней. Этого достаточно для регистрации."
    $bank_choice = False
    $mfc_choice = True
    $mfc_choice_index = 1

    jump choice_scene




label bank_chice_A:
    scene bank_scene_image with fade

    show expression player_backpack as player_sprite at pos_far_left_inactive
    show bank_specialist as bank_specialist at pos_far_right_inactive

    show expression player_backpack as player_sprite at pos_far_left_active with dissolve
    show bank_specialist as bank_specialist at pos_far_right_inactive with dissolve
    player "Вот мои основные документы: паспорт, справка 2-НДФЛ с текущей работы."
    player "Первоначальный взнос — 20%% от ориентировочной стоимости в 5 млн рублей. Давайте рассчитаем"

    show bank_specialist_writes as bank_specialist at pos_far_right_active with dissolve
    show expression player_backpack as player_sprite at pos_far_left_inactive with dissolve
    bankir "Отлично, введу данные"
    bankir "Вам предварительно одобрено 4 000 000 ₽ на 20 лет." 
    bankir "Ставка — 9%% годовых. Это решение действует 30 дней"

    show expression player_backpack as player_sprite at pos_far_left_active with dissolve
    show bank_specialist as bank_specialist at pos_far_right_inactive with dissolve
    player "Хорошо"

    $ grant_achievement("the_risk_overpayment")
    scene expression player_strit with fade
    "Вы получаете деньги в кредит, но ставка завышена, так как вы не предоставили доказательства дополнительных доходов или не сравнили условия других банков."
    "Пора идти к риелтору"
    $ grant_achievement("approved")
    $ bank_choice = False
    $ realtor_choice = True
    $ realtor_choice_index = 1
    jump choice_scene


label bank_chice_B:
    show expression player_backpack as player_sprite at pos_far_left_active with dissolve
    player "Прежде чем передать данные, кое-что уточню"
    player "Кроме 2-НДФЛ, учитываете ли вы справку по форме банка, заверенную работодателем?"
    player "Или данные из личного кабинета ФНС о доходах по форме 3-НДФЛ (для ИП/фрилансера)?"
    show bank_specialist_surprised as bank_specialist at pos_far_right_inactive with dissolve
    player "Для первоначального взноса я планирую использовать собственные сбережения, что подтверждается выпиской со счёта." 
    player "Это повлияет на ставку?"

    show bank_specialist_writes as bank_specialist at pos_far_right_active with dissolve
    show expression player_backpack as player_sprite at pos_far_left_inactive with dissolve
    bankir "Я вижу, вы подготовились. Да, форма банка или данные ФНС увеличат доверие."
    bankir "Да, форма банка или данные ФНС увеличат доверие."
    bankir "При взносе от 20%% и подтверждённом доходе мы можем рассмотреть сниженную ставку по акции или для зарплатных клиентов."
    show bank_specialist_writes as bank_specialist at pos_far_right_active with dissolve
    bankir "Давайте уточним детали»."

    $ grant_achievement("an_attentive_borrower")
    scene expression player_strit with fade
    "Вы увидели, что можете претендовать на ставку 8%% вместо 9%%, экономя ~500 000 ₽ за весь срок."
    "Теперь иожно вернуться к риелтору"
    $ grant_achievement("approved")
    $ realtor_choice = True
    $ realtor_choice_index = 1
    $ bank_choice = False
    jump choice_scene






# ========================================
# Сцена у риелтора с её исходами
# ========================================
label realtor_scene_0:
    scene realtor_interior_image with fade
    
    show expression player_backpack as player_sprite at pos_far_left_inactive
    show realtor_dmitriy as realtor_sprite at pos_far_right_inactive

    show expression player_backpack as player_sprite at pos_far_left_active with dissolve
    show realtor_dmitriy as realtor_sprite at pos_far_right_inactive with dissolve
    player "Добрый день! Я хочу приобрести квартиру"

    show realtor_dmitriy as realtor_sprite at pos_far_right_active with dissolve
    show expression player_backpack as player_sprite at pos_far_left_inactive with dissolve
    character_realtor "На какой бюджет вы рассчитываете?"

    show expression player_backpack as player_sprite at pos_far_left_active with dissolve
    show realtor_dmitriy as realtor_sprite at pos_far_right_inactive with dissolve
    player "У меня есть 500000 руб. Что можно подобрать на данную сумму?"

    show realtor_dmitriy_laughter as realtor_sprite at pos_far_right_active with dissolve
    show expression player_perplexity as player_sprite at pos_far_left_inactive with dissolve
    character_realtor "На такую сумму можно купить только собачью будку!"
    character_realtor "Для покупки квартиры необходимо как минимум в 10 раз больше."

    show realtor_dmitriy as realtor_sprite at pos_far_right_active with dissolve 
    character_realtor "Буду искать для вас варианты, а вы думаете, где взять деньги."

    menu:
        "Как поступить?"

        "Взять кредит":
            $ bank_choice = True
            $ realtor_choice = False
            jump choice_scene

        "Украсть деньги":
            jump prison_scene
    

label realtor_scene_1:
    scene realtor_interior_image with fade
    
    show expression player_interested as player_sprite at pos_far_left_inactive
    show realtor_dmitriy_display as realtor_sprite at pos_far_right_inactive

    show realtor_dmitriy_display as realtor_sprite at pos_far_right_active with dissolve
    show expression player_interested as player_sprite at pos_far_left_inactive with dissolve
    character_realtor "Смотрите, вот он — идеальный вариант для первого жилья или инвестиций!"
    character_realtor "Хозяйка — милейшая женщина — срочно уезжает в Германию на ПМЖ. Поэтому цена просто смешная: 7.2 млн вместо реальных 9!"
    character_realtor "Но есть нюанс..."
    character_realtor "Уже завтра утром придут другие покупатели. Я их, конечно, могу задержать, но мне нужны гарантии с вашей стороны."
    character_realtor "Можете сегодня же внести задаток 300 000, чтобы я снял квартиру с продажи?"
    character_realtor "Мы с хозяйкой уже договорились — кто первый с деньгами, того и квартира!"
    
    menu:
        "Как поступить?"

        "Отдать задаток":
            jump give_deposit
            
        "Проверить документы":
            jump check_documents

#Проверить документы
label check_documents:
    show expression player_backpack as player_sprite at pos_far_left_active with dissolve
    show realtor_dmitriy_display as realtor_sprite at pos_far_right_inactive with dissolve
    player "Сначала хочу увидеть оригиналы документов собственника и выписку из ЕГРН."
    player "Задаток внесу только после проверки и только по договору задатка с указанием условий возврата."

    show realtor_dmitriy_surprised as realtor_sprite at pos_far_right_active with dissolve
    show expression player_backpack as player_sprite at pos_far_left_inactive with dissolve
    character_realtor "Э... конечно, документы у хозяйки."

    show expression player_backpack as player_sprite at pos_far_left_active with dissolve
    show realtor_dmitriy_upset as realtor_sprite at pos_far_right_inactive with dissolve
    player "Я понимаю. Но без проверки и без договора с собственником я деньги не передаю."
    player "Если квартира уйдёт — значит, не моё."

    show realtor_dmitriy_upset as realtor_sprite at pos_far_right_active with dissolve
    show expression player_backpack as player_sprite at pos_far_left_inactive with dissolve
    character_realtor "Ну, как хотите. Я предупредил."

    scene expression player_strit with fade
    "Деньги удалось сохранить: покупатель не подписал сомнительных бумаг.
    Сделка сорвалась, но всё обошлось без потерь."
    jump choice_scene
    $ realtor_choice = False


#Отдать задаток за квартиру сразу
label give_deposit:
    show expression player_backpack as player_sprite at pos_far_left_active with dissolve
    show realtor_dmitriy_display as realtor_sprite at pos_far_right_inactive with dissolve
    player "Да, квартира и правда отличная!"
    player "Слишком хороший шанс, чтобы упускать."
    
    show expression player_maney as player_sprite at pos_far_left_active with dissolve
    player "Вот 300 000 наличными, как вы и просили."

    show realtor_dmitriy as realtor_sprite at pos_far_right_active with dissolve
    show expression player_backpack as player_sprite at pos_far_left_inactive with dissolve
    character_realtor "Правильное решение!"
    character_realtor "Поздравляю, теперь квартира ваша!"

    show realtor_dmitriy_record as realtor_sprite at pos_far_right_active with dissolve
    character_realtor "Сейчас я напишу расписку, все по-честному."

    
    scene expression player_receipt with fade
    "Он протягивает вам листок. Подписи хозяина нет, печати тоже."

    scene realtor_interior_image with fade
    show expression player_backpack as player_sprite at pos_far_left_active with dissolve
    show realtor_dmitriy_display as realtor_sprite at pos_far_right_inactive with dissolve
    player "А где условия, если вдруг что-то пойдет не так? И где подпись собственника?"

    show expression player_backpack as player_sprite at pos_far_left_inactive with dissolve
    show realtor_dmitriy_display as realtor_sprite at pos_far_right_active with dissolve
    character_realtor "Да всё будет хорошо! Хозяйка уже дала добро"
    character_realtor "Это же просто формальность для наших юристов. Забирайте ключи!"
    character_realtor "Точнее, ключи я вам передам завтра, после того как оформлю документы у нее. Главное — квартира ваша!"

    scene realtor_bilding_image with fade
    show expression player_agency as player_sprite at pos_far_right_active with dissolve
    "Вы приходите в офис агентства Мечта в 10 утра, как договорились. Офис закрыт. На двери табличка Технический перерыв."

    show expression player_call as player_sprite at pos_far_right_active with dissolve
    show realtor_dmitriy_call as realtor_sprite at pos_far_left_inactive with dissolve
    player "Дмитрий, добрый день, я у офиса. Мы же договаривались?"

    show expression player_call as player_sprite at pos_far_right_inactive with dissolve
    show realtor_dmitriy_call as realtor_sprite at pos_far_left_active with dissolve
    character_realtor "А, здравствуйте. По вашей ситуации... К сожалению, хозяйка передумала."
    character_realtor "Решила не продавать квартиру. Или продать другому. В общем, сделка не состоится."
    
    show expression player_call as player_sprite at pos_far_right_active with dissolve
    show realtor_dmitriy_call as realtor_sprite at pos_far_left_inactive with dissolve
    player "Как не состоится?! А мои 300 000? Возвращайте деньги!"

    show expression player_call as player_sprite at pos_far_right_inactive with dissolve
    show realtor_dmitriy_call as realtor_sprite at pos_far_left_active with dissolve
    character_realtor "Какие деньги? Вы же вчера внесли аванс. Аванс, в случае отказа покупателя от сделки, не возвращается. Вы отказываетесь — деньги наши. Всё по расписке."

    show expression player_call as player_sprite at pos_far_right_active with dissolve
    show realtor_dmitriy_call as realtor_sprite at pos_far_left_inactive with dissolve
    player "Но отказываетесь вы, а не я! И это был задаток!"

    show expression player_call as player_sprite at pos_far_right_inactive with dissolve
    show realtor_dmitriy_call as realtor_sprite at pos_far_left_active with dissolve
    character_realtor "В расписке черным по белому написано: 'в качестве аванса'. Задаток должен был оформляться отдельным договором с собственником. У вас его нет. Все претензии — к хозяйке, а она, как я говорил, уже в Германии. Удачи."

    scene expression player_crying with fade
    
    "Сделка сорвалась… но деньги уже не вернуть."

    "Вы потеряли 300 000 рублей — все свои накопления."
    "Расписка оказалась недействительной."
    "Стресс и чувство обмана накрывают с головой."

    "Полиция принимает заявление, но предупреждает — шансы найти мошенников минимальны."

    pause 1.0

    "Вы стали жертвой."

    pause 1.0

    jump lesson_scene

label lesson_scene:
    $ realtor_choice = False
    $ mfc_choice = True
    call screen lesson_popup
    
    if _return == "choice_scene":
        jump choice_scene

screen lesson_popup():
    add "gui/select_bg.jpg"
    modal True
    zorder 200

    add Solid("#000000aa")

    frame:
        xalign 0.5
        yalign 0.5
        xsize 700
        padding (30, 25)
        background "#b4b1b1ee"
        

        vbox:
            spacing 15

            text "Урок" size 36 bold True xalign 0.5

            text "Аванс — это риск.\nЗадаток — это договор с ответственностью сторон.\nНикогда не передавайте деньги риелтору без проверки документов и участия собственника.":
                
                color "#333333"

            text "Благодаря полученному опыту вам доступны новые действия:"
                

            text "Проверить собственника через МФЦ\n• Рассмотреть покупку у застройщика":
               
                color "#444444"
        
            textbutton "Продолжить":
                xalign 0.5
                action Return("choice_scene")  
    
   


# ========================================
# Сцена у Юриста с её исходами
# ========================================
label lawyer_scene:
        scene notary_bilding with fade
        "После проверки документов в МФЦ и подтверждения, что продавец — реальный собственник, наступает этап юридического оформления задатка и предварительного договора."
        "От того, как будут прописаны условия, зависит, сможет ли ты вернуть деньги в случае срыва сделки."

        menu:
            "Юрист поможет вам избежать типичных ошибок и составит договор с защитой ваших интересов"
            "Нанять юриста?"

            "Отдать 15.000₽ за юриста":
                $lawyer_hire = True
            
            "Справлюсь сам":
                $lawyer_hire = False

        scene notary_bilding_interior with fade
        show expression player_backpack as player_sprite at pos_far_right_inactive with dissolve
        show seller_character as seller_character at pos_far_left_active with dissolve
        seller "Ну что, я предлагаю не тянуть. Давайте внесёте задаток 100 000 рублей, я напишу расписку, и будем считать, что договорились."
            
        if lawyer_hire:
            show lawyer_character as player_sprite at pos_far_right_active with dissolve
            show seller_character as seller_character at pos_far_left_inactive with dissolve
            lawyer "Это риск. Расписка без договора — это аванс, а не задаток."
            lawyer "При срыве сделки по вине продавца вы получите только сумму обратно, без штрафа"

            show lawyer_character as player_sprite at pos_far_right_inactive with dissolve
            show seller_character as seller_character at pos_far_left_active with dissolve
            seller "Это слишком жестко. Я могу просто передумать продавать, а вы получите назад только ваш задаток без компенсации."

            show lawyer_character as player_sprite at pos_far_right_active with dissolve
            show seller_character as seller_character at pos_far_left_inactive with dissolve
            lawyer "Коллега, такие условия — стандартная практика для защиты обеих сторон. Это не доверие, а юридическая гарантия." 
            lawyer "Если вы откажетесь без оснований, покупатель получит\n200 000 рублей. Это мотивирует исполнить обязательства. "

            show lawyer_character as player_sprite at pos_far_right_inactive with dissolve
            show seller_character as seller_character at pos_far_left_active with dissolve
            seller "Хорошо я согласна, довайте составим договор"

            $ grant_achievement("legally_savvy")
            scene notary_bilding with fade
            show expression player_backpack_doc as player_sprite at pos_far_left_active with dissolve
            "У вас на руках предварительный договор с защитой, вы смогли себя обезопасить"
            "Хорошобы положить деньги в банк для передачи"
            $ lawyer_choice = False
            $ bank_choice = True
            $ bank_choice_index = 1
            jump choice_scene
            


        else:
            scene notary_bilding with fade
            show expression player_backpack_doc as player_sprite at pos_far_left_active with dissolve
            "Вы выбрали самый рискованный вариант. При срыве сделки вы не сможете взыскать штраф"
            "Хорошобы положить деньги в банк для передачи"
            $ lawyer_choice = False
            $ bank_choice = True
            $ bank_choice_index = 1
            jump choice_scene
    

label prison_scene:
    scene expression player_robbery with fade
    "Во время ограбления сработала сигнализация и вас поймали"
    scene expression player_prison with fade
    "по ст. 158 УК РФ вы осуждены на срок 10 лет"

label test_map:
    scene test_image
    "Нас плохо кормить, но мы стараться написать история"