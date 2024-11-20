from Projeto_Blog.Blog import show_menu, add_post, add_user, query_users_posts

while True:
    show_menu()
    option = input('Selecione uma opção: ')

    if option == '1':
        add_user()
    elif option == '2':
        add_post()
    elif option == '3':
        query_users_posts()