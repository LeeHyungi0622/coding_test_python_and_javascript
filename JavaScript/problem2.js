// stone_durability = [1, 2, 1, 4]
const stone_durability = [5, 3, 4, 1, 3, 8, 3];
const dog = [{
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
}, ]

function crossTheStoneBridge(dur, dog) {
    answer = [];
    for (let individual_dog of dog) {
        let dog_position = 0;
        let fail = false;
        while (dog_position < dur.length) {
            dog_position += parseInt(individual_dog['jump'], 10);
            dur[dog_position - 1] -= parseInt(individual_dog['weight'], 10);
            if (dur[dog_position - 1] < 0) {
                fail = true;
                break;
            }
        }
        if (!fail) {
            answer.push(individual_dog['name']);
        }
    }

    // 점프력이 2이면, 돌의 index가 1인 위치에서 멈추므로, 점프력-1 위치의 돌에서
    // 개의 몸무게만큼 내구력을 차감시킨다.
    // 내구도가 0이하이면 물에 빠진다.


    return answer
}

console.log(crossTheStoneBridge(stone_durability, dog));