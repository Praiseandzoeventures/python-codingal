student_data = {
    "id1" : {
        "name":"Sara",
        "class":"V",
        "subject":["english,math,science"]
    },
     "id2" : {
        "name":"Daniel",
        "class":"V",
        "subject":["english,math,science"]
    },
     "id3" : {
        "name":"Sara",
        "class":"V",
        "subject":["english,math,science"]
    },
     "id4" : {
        "name":"John",
        "class":"V",
        "subject":["english,math,science"]
    }
}

result ={}
for key ,vaule in student_data.items():
    if vaule not in result.values():
        result[key]=vaule
print(result)