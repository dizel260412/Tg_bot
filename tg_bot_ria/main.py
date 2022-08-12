import config
from get_first_news import get_first_news
from config import url_dict


def main():
    headers = config.headers
    i = int(input(f'Мир - 1\nФутбол - 2\nЭкономика - 3\nПроишествия - 4\nНаука - 5\nКультура - 6\nРелигия - 7\n'
                  f'Туризм - 8\n'))
    try:
        url = url_dict[i - 1]
        dict_name = url.split('/')[-2]
        get_first_news(headers, url, dict_name)
    except Exception as ex:
        print('Проверьте правильность ввода!')
        main()


if __name__ == '__main__':
    main()
