def fill(text):
    line_lst = []
    for num, line in enumerate(text.split("\n")):
        str_lst = line.split(",")
        # print(str_lst)
        if num == 0:
            line_lst.append(str_lst)
        else:
            for num, str in enumerate(str_lst):
                if not str:
                    str_lst[num] = str_lst_last[num]
            line_lst.append(str_lst)
        str_lst_last = str_lst
    return line_lst


def notes2json(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        text = f.read()
    line_lst = fill(text)

    target_json = {}
    for num, line in enumerate(line_lst):
        if num == 0:
            container = target_json
            for str_ in line:
                if isinstance(container, dict):
                    container[str_] = []
                    container = container[str_]
                elif isinstance(container, list):
                    dic_ = {str_:[]}
                    container.append(dic_)
                    container = dic_[str_]
        else:
            container = target_json
            for str_ in line:
                if isinstance(container, dict):
                    if str_ in container.keys():
                        container = container[str_]
                elif isinstance(container, list):
                    if str_ in [list(dic_.keys())[0] for dic_ in container]:
                        for dic_ in container:
                            if str_ in dic_.keys():
                                container = dic_[str_]
                                break
                    else:
                        dic_ = {str_:[]}
                        container.append(dic_)
                        container = dic_[str_]
    return target_json



def foo(container, key, path_seg_all):
    path_seg = []
    path_seg.extend(path_seg_all)
    if isinstance(container, dict):
        if key in container.keys():
            path_seg.append(list(container.keys())[0])
            return path_seg
        else:
            path_seg.append(list(container.keys())[0])
            container = container.get(list(container.keys())[0])
            path_seg = foo(container, key, path_seg)
            if path_seg:
                return path_seg
    elif isinstance(container, list):
        if container:
            for dic_ in container:
                if key in dic_.keys():
                    path_seg = []
                    path_seg.extend(path_seg_all)
                    path_seg.append(list(dic_.keys())[0])
                    return path_seg
                else:
                    container = dic_
                    path_seg = []
                    path_seg.extend(path_seg_all)
                    path_seg = foo(container, key, path_seg)
                    if path_seg:
                        return path_seg
        else:
            path_seg = []


def find(target_json, key):
    path_seg = foo(target_json, key, [])
    if path_seg:
        path_seg = ".".join(path_seg)
    else:
        path_seg = "不存在关键字：{0}".format(key)
    return path_seg





def main():
    target_json = notes2json("./concepts.txt")
    print(target_json)
    print('\n\n')


    key = "感知机"
    path = find(target_json, key)
    print(path)
    print('\n\n')


    key = "贝叶斯模型"
    path = find(target_json, key)
    print(path)
    print('\n\n')
























































if __name__ == "__main__":
    main()
