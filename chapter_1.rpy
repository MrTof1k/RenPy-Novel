# ========================================
# ОСНОВНАЯ ИСТОРИЯ Главы 1 (квартира)
# ========================================
label story_kv:
    default mfc_choice = False
    default bank_choice = False
    default realtor_choice = True 
    default lawyer_choice = False
    default yk_choice = False
    default mfc_choice_index = 0
    default bank_choice_index = 0
    default realtor_choice_index = 0
    default lawyer_hire = False

    $ grant_achievement("first_start")
    $ player = Character(player_name, color="#c8ffc8")
    
    show expression player_think
    "Ты закончил институт, устраиваешься на работу, следующий этап- покупка квартиры."
    "Надо сходить к риелтору!"
    hide expression player_think with dissolve
    
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

        elif _return == "yk" and yk_choice:
            jump test_map

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
        show mfc_holl_2 with fade
        "Сделка согласована, деньги в ячейке, документы подписаны."
        " Остался последний юридический шаг — регистрация права собственности в Росреестре."

        show expression player_backpack_doc as player_sprite at pos_far_left_inactive with dissolve
        show mfc_character_doc as mfc_character_doc at pos_far_right_active with dissolve
        mfc "Приём документов на регистрацию перехода права собственности."
        mfc "Проверяю ваш пакет: заявления обеих сторон, ДКП в трёх экземплярах, паспорта, квитанция об оплате госпошлины, акт приёма-передачи…"
        mfc "Всё в порядке. Распишитесь в реестре. Срок оказания услуги — 9 рабочих дней. Вы получите уведомление на email."

        show expression player_backpack_doc as player_sprite at pos_far_left_active with dissolve
        show seller_character as mfc_character_doc at pos_far_right_inactive with dissolve
        player "Спасибо. Что нам делать с ключами от квартиры?"

        show expression player_backpack_doc as player_sprite at pos_far_left_inactive with dissolve
        show seller_character as mfc_character_doc at pos_far_right_active with dissolve
        seller "Я передам их вам прямо сейчас, а вот забирать вещи буду в течение 5 дней, как и прописано в акте."
        seller "Вы же не против?"
        
        menu:
            "Хорошо, но оставьте, пожалуйста, расписку, что вещи будут вывезены":
                call screen mfc_scene_receipt
                
            
            "Ладно, верю вам на слово":
                call screen mfc_scene_no_receipt_screen

        
    else:
        jump test_map
    return

# label mfc_scene_receipt:
#     show expression player_mfc_receipt with fade
#     "Продавец пишет расписку с датой вывоза вещей и обязательством не оставлять мусор."
#     "Таким образом вы получили отсутствие конфликта после сделки"
#     jump mfc_scene_9_day

screen mfc_scene_receipt:
    
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

            text "Итог" size 36 bold True xalign 0.5

            text "Продавец пишет расписку с датой вывоза вещей и обязательством не оставлять мусор.":
                
                color "#333333"

            text "Сделав данный шаг"
                

            text "Вы получили отсутствие конфликта после сделки":
               
                color "#444444"
        
            textbutton "Продолжить":
                xalign 0.5
                action Jump("mfc_scene_9_day") 

screen mfc_scene_no_receipt_screen():
    
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

            text "Итог" size 36 bold True xalign 0.5

            text "Вы не взяли расписку у продавца.":
                color "#333333"

            text "Сделав данный шаг"
                

            text "Вы рискуете получить квартиру с чужими вещами или конфликтом после сделки.":
               
                color "#444444"
        
            textbutton "Продолжить":
                xalign 0.5
                action Jump("mfc_scene_9_day")


label mfc_scene_9_day:
    scene expression player_document with fade
    "Через 9 дней вам приходит письмо"
    "В нем сказано, что: Право собственности зарегистрировано. Номер записи в ЕГРН: 77:01:0001234:567."
    $ grant_achievement("homeowner")
    $ mfc_choice = False
    $ yk_choice = True
    jump choice_scene

    

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
    
    $ realtor_choice = False
    jump choice_scene


#Отдать задаток за квартиру сразу
label give_deposit:
    # --- Сцена передачи денег ---
    show expression player_maney as player_sprite at pos_far_left_active with dissolve
    show realtor_dmitriy_display as realtor_sprite at pos_far_right_inactive with dissolve
    
    player "Да, квартира и правда отличная!"
    player "Слишком хороший шанс, чтобы упускать. Вот 300 000 наличными, как вы и просили."
    
    "Вы передаете пачку купюр. Глаза Дмитрия загораются, но он быстро берет себя в руки."
    
    show realtor_dmitriy as realtor_sprite at pos_far_right_active with dissolve
    character_realtor "Правильное решение! Поздравляю, теперь квартира фактически ваша!"
    character_realtor "Осталось только закрепить это на бумаге."

    show realtor_dmitriy_record as realtor_sprite at pos_far_right_active with dissolve
    "Он хватает бланк и начинает быстро писать, не поднимая глаз."
    
    character_realtor "Сейчас я напишу расписку, все по-честному. Подписывайте здесь, здесь и здесь."
    character_realtor "Торопитесь, у меня еще встречи."

    scene expression player_receipt with fade
    "Он протягивает вам смятый листок. Почерк неразборчивый."
    "Подписи хозяйки нет. Печати агентства тоже нет. Только подпись Дмитрия."

    scene realtor_interior_image with fade
    show expression player_backpack as player_sprite at pos_far_left_active with dissolve
    show realtor_dmitriy_display as realtor_sprite at pos_far_right_inactive with dissolve
    
    player "Постойте... А где условия? Что будет, если сделка сорвется?"
    player "И где подпись собственника? Вы же говорили, что она в курсе?"

    show expression player_backpack as player_sprite at pos_far_left_inactive with dissolve
    show realtor_dmitriy_display as realtor_sprite at pos_far_right_active with dissolve
    
    character_realtor "Ой, ну вы начинаете..."
    character_realtor "Хозяйка уже дала мне доверенность на словах. Она в Германии, ей сейчас не до бумаг."
    character_realtor "Это же просто формальность для наших юристов. Забирайте ключи!"
    
    "Он сует вам в руку связку ключей, но тут же забирает их обратно."
    
    character_realtor "Точнее, ключи я вам передам завтра, после того как оформлю финальные документы у нее."
    character_realtor "Главное — квартира ваша! Жду вас завтра в 10:00 в офисе."

    # --- На следующее утро ---
    scene realtor_bilding_image with fade
    show expression player_agency as player_sprite at pos_far_right_active with dissolve
    
    "На следующее утро вы приезжаете к офису агентства «Мечта»."
    "Офис закрыт. На стеклянной двери висит самодельная табличка: «Технический перерыв до 15:00»."
    
    "Вы стоите на улице. Проходит 10 минут. Потом 20. Никого нет."
    "Вы решаете позвонить Дмитрию."

    show expression player_call as player_sprite at pos_far_right_active with dissolve
    
    "Гудки... Гудки..."
    "Наконец, трубку берут."

    show realtor_dmitriy_call as realtor_sprite at pos_far_left_inactive with dissolve
    
    player "Дмитрий? Добрий день, я у офиса. Мы же договаривались на 10 утра!"
    
    show expression player_call as player_sprite at pos_far_right_inactive with dissolve
    show realtor_dmitriy_call as realtor_sprite at pos_far_left_active with dissolve
    
    "Голос в трубке звучит холодно и отстраненно. Никакой вчерашней дружелюбности."
    
    character_realtor "А, здравствуйте. По вашей ситуации..."
    character_realtor "К сожалению, хозяйка передумала. Решила не продавать квартиру."
    character_realtor "Или продать другому. В общем, сделка не состоится. Извините."

    show expression player_call as player_sprite at pos_far_right_active with dissolve
    show realtor_dmitriy_call as realtor_sprite at pos_far_left_inactive with dissolve
    
    player "Как не состоится?! А мои 300 000?! Возвращайте деньги немедленно!"
    
    show expression player_call as player_sprite at pos_far_right_inactive with dissolve
    show realtor_dmitriy_call as realtor_sprite at pos_far_left_active with dissolve
    
    character_realtor "Какие деньги? Вы, кажется, путаете термины."
    character_realtor "Вы же вчера внесли *аванс*. А аванс, в случае отказа покупателя или по взаимному согласию, не возвращается в двойном размере, как задаток."
    character_realtor "А так как хозяйка передумала, мы просто расторгаем договоренность. Деньги наши за бронирование."

    show expression player_call as player_sprite at pos_far_right_active with dissolve
    show realtor_dmitriy_call as realtor_sprite at pos_far_left_inactive with dissolve
    
    player "Но отказываетесь ВЫ, а не я! И это был ЗАДАТОК! Вы так сказали!"
    
    show expression player_call as player_sprite at pos_far_right_inactive with dissolve
    show realtor_dmitriy_call as realtor_sprite at pos_far_left_active with dissolve
    
    character_realtor "В расписке черным по белому написано: 'в качестве аванса'. Я зачитывал вам?"
    character_realtor "Задаток должен был оформляться отдельным трехсторонним договором с собственником. У вас его нет."
    character_realtor "Все претензии — к хозяйке, а она, как я говорил, уже в Германии. И номера вы её не знаете."
    character_realtor "Удачи, не поминайте лихом."

    "Гудки."
    
    scene expression player_crying with fade
    "Вы опускаете телефон. Руки дрожат."
    
    "Сделка сорвалась… но деньги уже не вернуть."
    "Вы потеряли 300 000 рублей — все свои накопления."
    "Расписка оказалась недействительной ловушкой."
    
    "Стресс и чувство обмана накрывают с головой. Как можно было так легко повестись на 'смешную цену'?"
    
    pause 1.0
    
    "Полиция принимает заявление, но предупреждает — найти мошенников, работающих по такой схеме, почти невозможно."
    "Дмитрий — подставное лицо, а квартиры, скорее всего, не существует."

    pause 1.0
    
    "Вы стали жертвой."

    # Фиксируем переменные перед переходом к уроку
    $ realtor_choice = False
    $ mfc_choice = True # Открываем доступ к МФЦ как к безопасному пути
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
    
    "Офис нотариуса пахнет старой бумагой и дорогим кофе. Здесь царит атмосфера строгости и закона."
    "После проверки документов в МФЦ и подтверждения, что продавец — реальный собственник, наступает самый важный этап."
    "Этап юридического оформления задатка и предварительного договора."
    "От того, как будут прописаны условия в этих документах, зависит, сможете ли вы вернуть деньги, если сделка сорвется по вине продавца."
    

    menu:
        "Юрист поможет вам избежать типичных ошибок и составит договор с максимальной защитой ваших интересов."
        "Нанять юриста?"

        "Отдать 15.000₽ за услуги юриста":
            $ lawyer_hire = True
            "Вы решаете не экономить на безопасности. Лучше перестраховаться сейчас, чем потерять миллионы потом."
            
        "Справлюсь сам, зачем платить?":
            $ lawyer_hire = False
            "Вы уверенны в своих силах. Типовой договор из интернета должен подойти. К тому же, 15 тысяч — это тоже деньги."

    scene notary_bilding_interior with fade
    
    # --- Начало сцены переговоров ---
    
    show expression player_backpack as player_sprite at pos_far_right_inactive with dissolve
    show seller_character as seller_character at pos_far_left_active with dissolve
    
    seller "Ну что, давайте не будем тянуть время. Рынок сейчас горячий."
    seller "Я предлагаю внести задаток 100 000 рублей прямо сейчас. Я напишу простую расписку от руки, и будем считать, что квартира забронирована за вами."
    
    "Продавец улыбается, но её глаза внимательно следят за вашей реакцией. Она торопит события."
    
    if lawyer_hire:
        # --- Ветка с Юристом ---
        
        show lawyer_character as player_sprite at pos_far_right_active with dissolve
        show seller_character as seller_character at pos_far_left_inactive with dissolve
        
        lawyer "Стоп. Давайте остановимся на этом моменте."
        lawyer "Расписка от руки — это хорошо для фиксации факта передачи денег. Но это не защищает покупателя от рисков."
        
        show seller_character as seller_character at pos_far_left_active with dissolve
        show lawyer_character as player_sprite at pos_far_right_inactive with dissolve
        
        seller "Каких ещё рисков? Я же живой человек, я никуда не денусь!"
        seller "Зачем нам эти сложные бумажки? Мы же люди, а не роботы."
        
        show lawyer_character as player_sprite at pos_far_right_active with dissolve
        show seller_character as seller_character at pos_far_left_inactive with dissolve
        
        lawyer "Именно потому, что мы люди, эмоции могут взять верх над разумом. Или появится покупатель, который предложит больше."
        lawyer "Если вы подпишете только расписку, то юридически это считается *авансом*. Аванс подлежит возврату в любом случае, даже если продавец передумает."
        lawyer "Вы потеряете время, нервы и упущенную выгоду. А продавец отделается легким испугом."
        
        show seller_character as seller_character at pos_far_left_active with dissolve
        show lawyer_character as player_sprite at pos_far_right_inactive with dissolve
        
        seller "Ну... допустим. Но я не хочу никаких штрафов! Это слишком жестко."
        seller "Вдруг у меня форс-мажор случится? Мне что, платить вам полмиллиона?"
        
        show lawyer_character as player_sprite at pos_far_right_active with dissolve
        show seller_character as seller_character at pos_far_left_inactive with dissolve
        
        lawyer "Мы пропишем четкие условия. Задаток обеспечивает исполнение обязательства."
        lawyer "Если продавец отказывается от сделки без уважительной причины — он возвращает вам задаток в двойном размере."
        lawyer "Это стандартная практика ГК РФ. Это мотивирует исполнить обязательства, а не искать выгоду на стороне."
        lawyer "Если же откажетесь вы — задаток остается у продавца. Всё честно."
        
        show seller_character as seller_character at pos_far_left_active with dissolve
        show lawyer_character as player_sprite at pos_far_right_inactive with dissolve
        
        "Продавец хмурится, перечитывая проект договора, который протягивает ей юрист."
        "Пауза затягивается. Слышно только шуршание бумаг."
        
        seller "Хм... Двойной размер... Это неприятно."
        seller "Но если я ничего не нарушаю, то мне и бояться нечего, верно?"
        
        show lawyer_character as player_sprite at pos_far_right_active with dissolve
        show seller_character as seller_character at pos_far_left_inactive with dissolve
        
        lawyer "Верно. Договор защищает обе стороны. Он делает ваши отношения прозрачными."
        
        show seller_character as seller_character at pos_far_left_active with dissolve
        show lawyer_character as player_sprite at pos_far_right_inactive with dissolve
        
        seller "Ладно. Вы правы. Лучше сделать всё по закону, чем потом бегать по судам."
        seller "Давайте составим нормальный предварительный договор с условием о задатке."

        $ grant_achievement("legally_savvy")
        
        scene notary_bilding with fade
        show expression player_backpack_doc as player_sprite at pos_far_left_active with dissolve
        
        "Юрист тщательно проверяет каждый пункт. Теперь у вас на руках документ, имеющий реальную юридическую силу."
        "Вы чувствуете себя спокойнее. Вас не так легко обмануть."
        
        "Теперь нужно решить вопрос безопасной передачи основной суммы."
        "Хорошо бы положить деньги в банк для передачи через ячейку или аккредитив."
        
        $ lawyer_choice = False
        $ bank_choice = True
        $ bank_choice_index = 1
        jump choice_scene

    else:
        # --- Ветка БЕЗ Юриста ---
        
        show expression player_backpack as player_sprite at pos_far_right_active with dissolve
        show seller_character as seller_character at pos_far_left_inactive with dissolve
        
        player "Давайте я сам посмотрю образец договора в интернете. Мне кажется, там всё просто."
        
        show seller_character as seller_character at pos_far_left_active with dissolve
        show expression player_backpack as player_sprite at pos_far_right_inactive with dissolve
        
        seller "Ой, ну конечно! Зачем вам этот юрист? Он же просто хочет денег содрать."
        seller "Мы с вами взрослые люди. Вот ручка, вот листок. Напишите: 'Получил от такого-то такую-то сумму в качестве задатка'. И подпись моя."
        
        "Продавец протягивает вам простой бланк. Он выглядит очень неофициально."
        
        show expression player_backpack as player_sprite at pos_far_right_active with dissolve
        show seller_character as seller_character at pos_far_left_inactive with dissolve
        
        player "А где тут пункт о ответственности? Что если вы передумаете продавать?"
        
        show seller_character as seller_character at pos_far_left_active with dissolve
        show expression player_backpack as player_sprite at pos_far_right_inactive with dissolve
        
        seller "Я не передумаю! У меня уже билеты куплены. Не переживайте вы так."
        seller "Подписывайте, пока я добрая. Другие покупатели звонят каждые пять минут."
        
        "Под давлением и спешкой вы подписываете документ. Вам кажется, что всё нормально."
        
        scene notary_bilding with fade
        show expression player_backpack_doc as player_sprite at pos_far_left_active with dissolve
        
        "Вы выходите из офиса с чувством выполненного долга, но легкой тревогой."
        "Вы выбрали самый рискованный вариант. В договоре нет четких механизмов защиты."
        "При срыве сделки вы сможете вернуть только свои 100 тысяч, но не получите компенсации за потраченное время и упущенные возможности."
        
        "Теперь нужно решить вопрос безопасной передачи основной суммы."
        "Хорошо бы положить деньги в банк для передачи через ячейку или аккредитив."
        
        $ lawyer_choice = False
        $ bank_choice = True
        $ bank_choice_index = 1
        jump choice_scene

label prison_scene:
    scene expression player_robbery with fade
    "Во время ограбления сработала сигнализация."
    "Вы попытались бежать, но охрана заблокировала выходы."
    "Полиция прибыла через 3 минуты."
    "Вас задержали без сопротивления."
    
    scene expression player_prison with fade
    "Суд состоялся через полгода."
    "по ст. 158 УК РФ вы осуждены на срок 10 лет лишения свободы."
    "Ваши мечты о квартире так и остались мечтами..."
    
    pause 2.0
    return

label test_map:
    scene test_image
    "Нас плохо кормить, но мы стараться написать история"