interface Person {
    first_name: string;
    last_name: string;
    age: number;
}

const me: Person = {
    first_name: 'Eric',
    last_name: 'Kersten',
    age: 38
};

console.log(me);
document.write(`${me.first_name} ${me.last_name} (${me.age})`);