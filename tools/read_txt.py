def read_txt(filename):
    with open("./data/"+filename,"r",encoding="utf-8") as f:
        arr = []
        for data in f.readlines():
            arr.append(tuple(data.strip().split(",")))
        return arr[1::]

if __name__ == '__main__':
    print(read_txt("employee_post.txt"))
