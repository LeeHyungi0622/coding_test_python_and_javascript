const wait_people = 14000605;

function timeOfCrossingByShip() {
    let year = 0,
        month = 0,
        day = 0,
        hour = 0,
        min = 0;

    const takenDays = wait_people / 1200;
    let one_year_days = 0;
    for (let i = 1; i < 11; i++) {
        one_year_days += 2 ** i;
    }
    year = parseInt((wait_people / 1200) / one_year_days, 10)
    let rest_days = (wait_people / 1200) % one_year_days;
    month = 0;
    for (let i = 10; i > 0; i--) {
        month++;
        if (rest_days < 2 ** i) {
            break
        }
        rest_days -= 2 ** i;
    }
    day = parseInt(rest_days, 10);
    month = parseInt(month - 1, 10);
    hour = parseInt((wait_people % 1200) / 100 + 9, 10);
    const minute_list = [25, 40, 55, 70, 85, 100];
    let calculated_min = 0;
    for (let idx in minute_list) {
        if (minute_list[idx] > (wait_people % 1200) % 100) {
            calculated_min = idx * 10;
            break
        }
    }
    let date = new Date();
    calculated_min += date.getMinutes();

    if (calculated_min > 60) {
        calculated_min -= 60;
        hour += 1;
    }
    min = calculated_min;
    return `${year}년${month}월${day}일 ${hour}:${min}`;
}

console.log(timeOfCrossingByShip(wait_people));