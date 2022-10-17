import json
import models


with open("rasp.json", encoding="utf8") as file:
    datas = file.read()


def get_faculties(data: dict) -> list[models.Faculties]:
    faculties = []
    for i in range(len(data["faculties"])):
        faculties.append(models.Faculties(id=i,
                                faculty_name=data["faculties"][i]["faculty_name"],
                                date_start=data["faculties"][i]["date_start"],
                                date_end=data["faculties"][i]["date_end"],
                                groups=None
                                ))
    return faculties


def get_all(data: list[models.Faculties]):
    print(data[0].groups)


if __name__=="__main__":
    a = models.JSON_Faculties.parse_raw(datas)
    print(a)

#    print(a)