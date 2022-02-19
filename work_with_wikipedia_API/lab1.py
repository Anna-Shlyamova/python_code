import wikipedia


def is_page_valid(page):
    try:
        wikipedia.page(page)
    except Exception:
        return False
    return True


def language(ln):
    if ln in wikipedia.languages():
        return True
    else:
        return False


def maximum(names):
    maxi = 0
    title = ''
    for i in range(len(names)):
        page = wikipedia.page(names[i])
        sum = len(page.summary.split())
        if sum >= maxi:
            maxi = sum
            title = page.title
    return str(maxi) + (' ') + (title)


def chain(names):
    ch = [names[0]]
    for z in range(len(names) - 1):
        links = wikipedia.page(names[z]).links
        if names[z + 1] in links:
            ch.append(names[z + 1])
        else:
            for j in range(len(links)):
                if is_page_valid(links[j]):
                    if names[z + 1] in wikipedia.page(links[j]).links:
                        ch.append(links[j])
                        ch.append(names[z + 1])
                        break
    return ch


inp = input().split(', ')
lan = inp.pop()
if language(lan):
    wikipedia.set_lang(lan)
    titles = []
    for i in range(len(inp)):
        if is_page_valid(inp[i]):
            titles.append(inp[i])
    print(maximum(titles))
    print(chain(titles))
else:
    print("no results")


