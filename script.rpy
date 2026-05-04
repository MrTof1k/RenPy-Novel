init python:
    config.game_menu_action = ShowMenu("pause_menu")
    #Отладка достижений
    # persistent.unlocked_achievements = []
    # renpy.save_persistent()
    # renpy.notify("Достижения сброшены.")

    

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
    player_mfc_receipt = "artem_mfc_receipt"
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
    image artem_mfc_receipt = "Images/artem_scene/artem_mfc_receipt.png"
    image artem_crying = "Images/artem_scene/artem_crying.png"
    image artem_mfc = "Images/artem_scene/artem_mfc.png"
    image artem_mfc_tiket = "Images/artem_scene/artem_mfc_tiket.png"
    image artem_mfc_window = "Images/artem_scene/artem_mfc_window.png"
    image artem_document = "Images/artem_scene/artem_document.png"

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
    image elin_mfc_receipt = "Images/elin_scene/elin_mfc_receipt.png"
    image elin_crying = "Images/elin_scene/elin_crying.png"
    image elin_mfc = "Images/elin_scene/elin_mfc.png"
    image elin_mfc_tiket = "Images/elin_scene/elin_mfc_tiket.png"
    image elin_mfc_window = "Images/elin_scene/elin_mfc_window.png"
    image elin_document = "Images/elin_scene/elin_document.png"

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
    image mfc_holl_2 = "Images/mfc/mfc_holl_2.png"
    image mfc_character_doc = "Images/mfc/mfc_character_doc.png"

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
                SetVariable("player_mfc_receipt", "artem_mfc_receipt"),
                SetVariable("player_agency", "artem_agency"),
                SetVariable("player_call", "artem_call"),
                SetVariable("player_crying", "artem_crying"),
                SetVariable("player_mfc", "artem_mfc"),
                SetVariable("player_mfc_tiket", "artem_mfc_tiket"),
                SetVariable("player_mfc_window", "artem_mfc_window"),
                SetVariable("player_document", "artem_document"),
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
                SetVariable("player_mfc_receipt", "elin_mfc_receipt"),
                SetVariable("player_agency", "elin_agency"),
                SetVariable("player_call", "elin_call"),
                SetVariable("player_crying", "elin_crying"),
                SetVariable("player_mfc", "elin_mfc"),
                SetVariable("player_mfc_tiket", "elin_mfc_tiket"),
                SetVariable("player_mfc_window", "elin_mfc_window"),
                SetVariable("player_document", "elin_document"),
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
