workers = {
    "Айрат" : {
        "інформація": "Це людина яка створила компанію Airat company",
        "посада": "генеральний деректор, менеджер проекту",
        "проекти" : ["Бот Айрат вимагатель", "Правдива лотерея", "По писку тому хто не платить", "Airat bank(Найліпший банк)", "Cheating course"],
        "досягнення": ["Створив геніальну фірму Airat company, надурив більше двох мілйонів людей"],
        "хобі": "Намахувати людей"
        
    },
    "Гомослав" : {
        "інформація": "Це людина яка слідкує за дискримінацією меншин в колективі",
        "посада": "слідкує за дискримінацією меншин в колективі",
        "проекти" : ["Веселі ігри Гомославчика", "Контроль за дискримінацією"],
        "досягнення": ["Створив ідеальний колектив без дескримінації"],
        "хобі": "Баскетбол"
    },
    "Крутік": {
        "інформація": "Популярний репер стидно має бути тому хто його не знає. Він тіки частково працює в компанії",
        "посада": "піар менеджер",
        "проекти": "Склав пісню про компанію",
        "досягнення": "Не раз попадав в форбс",
        "хобі": "Розвиватись інтелектуально слухаючи реп"
    },
    "Пісим": {
        "інформація": "Це людина яку саме більше не люблять в колективі. Пісим любе підлизатись до айрата і розказати щось не добре про своїх співробітників",
        "посада": "системний адмінстратор",
        "проекти": ["Диктаторський контроль", "Айрат ти найліпший"],
        "досягнення": ["Найліпший співробітник року", "Зробив найліпший контроль часу співробітників"],
        "хобі": "підлизуватись до айрата"
    },
    "Задротіус": {
        "інформація": "Це наймудріша людина та головний програміст компінії. Любе в робочий час грати в велику ігру Dota 2",
        "посада": "Програміст",
        "проекти": ["Бот Махмуд", "Написав код до Airat bank", "Diskriminota 2"],
        "досягнення": ["10k MMR", "Найліпший програміст року", "хороша людина"],
        "хобі": "Грати в велику і геніальну гру Dota 2"
    },
    "Попуск": {
        "інформація": "Його звати Михайло але так він записаний в базі. Головний тестувальник компанії, людина з низькою самоцінкою яка попала в поганий колектив де над нею всі іздіваються",
        "посада": "Тестувальник",
        "проекти": "Тестував більшість проектів Airat company",
        "досягнення": "Був попушчений більше тисячі раз",
        "хобі": "Готувати"
    },
    "Мурат": {
        "інформація": "Це брат айрата тому він має високе становище в компанії. Має завишену самоцінку то він назвав Михайла попуском. Зарплата в два рази більша ніж моя гавнюк",
        "посада": "Бізнес-аналітик",
        "проекти": ["Ideal Bussines", "Bussines course"],
        "досягнення": ["Не дав обвалитися бізнесу айрата", "Найбільше чсв в колективі"],
        "хобі": "дивитись в дзеркало"
    },
    "Їжак": {
        "інформація": "Погана людина курила всьо шо куриться, то через нього в офісі стоїть дим",
        "посада": "Дизайнер",
        "проекти": "Робив інтерфейс до всіх проектів Airat company",
        "досягнення": ["Курець року", "Найбільше раз з компанії включав пожарну сиганлізацію", "Дизайнер року"],
        "хобі": ["Курити", "Курити", "Курити"]
    },
    "Гайбат": {
        "інформація": "Другий брат айрата пияче як незнати шо але його не звілняють через то шо то брат айрата. Половину робочго дня нема на роботі другу половину пяний, знає як викрутись з поганої ситуації",
        "посада": "Маркетолог",
        "проекти": ["Airat Performance", "Genius marketing", "Рекламував більшість проектів Airat company"],
        "досягнення": ["Ніразу не зявлявся тверезий на роботу", "З його допомогою Airat bank став найпопулярнішим банком в країні", "Найліпший маркетолог року"],
        "хобі": "Пити пиво під футбол"
    }
    
}

print("Привіт! Це я бот Махмуд я зберігаю інформацію про робітників Airat company")
print("Ви можете дізнатись про посаду, проект, досягнення та інформацію про робітника")
print("Наші робітники: Айрат, Гомослав, Крутік, Пісим, Задротіус, Попуск, Мурат, Їжак, Гайбат")
action = input("1-посаду, 2-проекти, 3-якусь інформацію від його співробітників, 4-досягнення, 5-хобі 6-всьо хочу знати, 7-ніц не хочу знати")
while action != "7":
    surname = input("Прізвище робітника:")
    if surname not in workers:
        print("Такого робітника немає в компанії")
    elif action == "1":
        print(workers[surname]["посада"])
    elif action == "2":
        print(workers[surname]["проекти"])
    elif action == "3":
        print(workers[surname]["інформація"])
    elif action == "4":
        print(workers[surname]["досягнення"])
    elif action == "5":
        print(workers[surname]["хобі"])
    elif action == "6":
        print("посада:",workers[surname]["посада"])
        print("проекти:",workers[surname]["проекти"])
        print("інформація:",workers[surname]["інформація"])
        print("досягнення:",workers[surname]["досягнення"])
        print("хобі:",workers[surname]["хобі"])
    action = input("1-посаду, 2-проекти, 3-якусь інформацію, 4-досягнення, 5-хобі, 6-всьо хочу знати, 7-ніц не хочу знати")

print("Ну і вали")
    
    