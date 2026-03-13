# achievements.rpy

init python:
    # Список всех достижений
    ACHIEVEMENTS = {
        "first_start": {
            "title": "Первый шаг",
            "desc": "Вы запустили игру."
        },
        "the_risk_overpayment": {
            "title": "Риск переплаты",
            "desc": "Взять кредит на невыгодных условиях."
        },
        "an_attentive_borrower": {
            "title": "Внимательный заёмщик",
            "desc": "Выбить снижение ставки с 9% до 8%"
        },
        "approved": {
            "title": "Одобрено",
            "desc": "Взять кредит в банке"
        }
    }


    if persistent.unlocked_achievements is None:
        persistent.unlocked_achievements = []

    def has_achievement(achievement_id):
        return achievement_id in persistent.unlocked_achievements

    def get_achievements_count():
        unlocked = 0

        for achievement_id in ACHIEVEMENTS:
            if has_achievement(achievement_id):
                unlocked += 1

        total = len(ACHIEVEMENTS)

        return unlocked, total
    
    def grant_achievement(achievement_id):

        if achievement_id not in ACHIEVEMENTS:
            return

        if achievement_id in persistent.unlocked_achievements:
            return

        persistent.unlocked_achievements.append(achievement_id)
        renpy.save_persistent()

        data = ACHIEVEMENTS[achievement_id]

        # Скрываем прошлое уведомление, если оно ещё висит
        renpy.hide_screen("achievement_popup")

        # Показываем новое
        renpy.show_screen(
            "achievement_popup",
            title=data["title"],
            desc=data["desc"]
        )

        renpy.restart_interaction()

screen achievement_popup(title, desc):

    zorder 100

    frame:
        xalign 0.98
        yalign 0.05
        xsize 420
        ypadding 15
        xpadding 20

        background "#1a1a1add"

        at achievement_anim

        hbox:
            spacing 15

            add "gui/trophy.png" size (64,64)

            vbox:
                spacing 4

                text "Достижение получено!" size 22 color "#FFD700"

                text title size 28 bold True

                text desc size 18 color "#cccccc"

transform achievement_anim:

    alpha 0.0
    xoffset 200

    easein 0.3 alpha 1.0 xoffset 0

    pause 3.0

    easeout 0.5 alpha 0.0 xoffset 200