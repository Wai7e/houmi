if __name__ == "__main__":

    def get_words(array):
        with open(array, encoding='utf-8') as file:
            file_all = file.readlines()
            count = []
            for i in file_all:
                count.append(i.strip().split(' '))
            count_words = 0
            for k in range(len(count)):
                for n in range(len(count[k])):
                    count_words += 1
            # print(count)
            print(f'There {count_words} words!!!')

            weight = 0
            for n in range(len(count)):
                for j in range(len(count[n])):
                    weight += len(count[n][j])
            mid_weight = weight/count_words
            return f'Middle weight of words - {mid_weight} symbols'

    def get_abz(array):
        with open(array, encoding='utf-8') as f:
            f = f.readlines()

            count_abz = 0
            for i in f:
                if i == '':
                    continue
                else:
                    count_abz += 1
            return f'Num of abz = {count_abz}'

    def get_top_weight(array):
        with open(array, encoding='utf-8') as f:
            f = f.readlines()
            count = []
            for i in f:
                count.append(i.strip().split(' '))

            max_weight = 0
            for n in range(len(count)):
                for j in range(len(count[n])):
                    if len(count[n][j]) > max_weight:
                        max_weight = len(count[n][j])
                    else:
                        continue
            return f'Max weight = {max_weight}'

    def get_top_word(array):
        with open(array, encoding='utf-8') as f:
            f = f.readlines()
            count = []
            for i in f:
                count.append(i.strip().split(' '))
            counter = {}
            for i in range(len(count)):
                for n in range(len(count[i])):
                    for word in count[i]:
                        counter[word] = counter.get(word, 0) + 1
                max_count = max(counter.values())
                most_frequent = [k for k, v in counter.items() if v == max_count]
        return min(most_frequent)

    def get_top_simb(array):
        with open(array, encoding='utf-8') as f:
            f = f.readlines()
            count = []
            for i in f:
                count.append(i.strip().split(' '))

                counter = {}
                for i in range(len(count)):
                    for n in range(len(count[i])):
                        for k in range(len(count[i][n])):
                            for word in count[i][n][k]:
                                counter[word] = counter.get(word, 0) + 1
                        max_count = max(counter.values())
                        most_frequent = [k for k, v in counter.items() if v == max_count]
        return min(most_frequent)

    def replace(array):
        with open(array, encoding='utf-8') as f:
            f = f.readlines()
            count = []
            for i in f:
                count.append(i.strip().split(' '))

            for i in range(len(count)):
                for n in range(len(count[i])):
                    if count[i][n] == 'Анна':
                        count[i][n].replace(count[i][n], 'Anna')
                    if count[i][n] == 'Павловна':
                        count[i][n].replace(count[i][n], 'Pavlovna')
        return count

    def russian(array):
        with open(array, encoding='utf-8') as f:
            f = f.readlines()
            count = []
            for i in f:
                count.append(i.strip().split(' '))

            for i in range(len(count)):
                for n in range(len(count[i])):
                    if count[i][n] in 'qwertyuiopasdfghjklzxvbnmQWERTYUIOPASDFGHJKLZXCVBNM':
                        del count[i][n]
        return count


    print(get_words('book.txt'))
    print(get_abz('book.txt'))
    print(get_top_weight('book.txt'))
    print(get_top_word('book.txt'))
    print(russian('book.txt'))