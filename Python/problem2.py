# stone_durability = [1, 2, 1, 4]
stone_durability = [5, 3, 4, 1, 3, 8, 3]
dog = [{
    "name": "루비독",
    "age": "95년생",
    "jump": "3",
    "weight": "4",
}, {
    "name": "피치독",
    "age": "95년생",
    "jump": "3",
    "weight": "3",
}, {
    "name": "씨-독",
    "age": "72년생",
    "jump": "2",
    "weight": "1",
}, {
    "name": "코볼독",
    "age": "59년생",
    "jump": "1",
    "weight": "1",
},
]

# remove O(N), del O(1)
# dur (durability) : 내구도
# dog : 돌다리를 건너는 개의 객체정보
def crossTheStoneBridge(dur, dog):
    #  개의 이름에 대한 정보를 answer에 리스트 형태로 담는다.
    # answer = [dog[i]['name'] for i in range(len(dog))]
    answer = [ i['name'] for i in dog]
    for i in dog:
        dog_position = 0
        # dog의 위치는 0부터 시작하기때문에  돌의 내구도 리스트-1보다 크다면 모든 돌을 건넌 것이기 때문에
        # dog이 돌을 모두 건너기 직전까지 실행을 한다.
        while dog_position < len(dur)-1:
            # dog의 위치에 해당 개의 jump력만큼 더해준다. (문자열이므로 숫자로 Int cating)
            dog_position += int(i['jump'])
            dur[dog_position-1] -= int(i['weight'])
            # 건널때 밟은 돌의 내구도가 0보다 작다면, 물에 빠지게 된다.
            if dur[dog_position-1] < 0:
                # answer[answer.index(i['name'])] = 'fail'
                # del의 속도가 더 빠르므로 물에 빠진 개의 이름을 리스트에서 제거해준다.
                del answer[answer.index(i['name'])]
                # while문 탈출
                break
    return [i for i in answer if i != 'fail']

# 복사본을 넘겨줌으로써 원본데이터가 변하는 것을 막는다.
# list의 경우, 밖에 선언한 값까지 변경시킨다.
print(crossTheStoneBridge(stone_durability.copy(), dog.copy()))
