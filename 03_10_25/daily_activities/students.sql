use university
switched to db university
db["Teachers"].find()
db.Teachers.insertOne({teacher_id:101,name:"sheena",age:34,department:"AI",salary:30000})
{
  acknowledged: true,
  insertedId: ObjectId('68dfb3608b9ce1c3a0b87a75')
}
db.Teachers.insertOne({
  teacher_id: 102,
  name: "Arvind",
  age: 40,
  department: "Data Science",
  salary: 45000
});

db.Teachers.insertOne({
  teacher_id: 103,
  name: "Lata",
  age: 29,
  department: "Cybersecurity",
  salary: 32000
});

db.Teachers.insertOne({
  teacher_id: 104,
  name: "Manoj",
  age: 37,
  department: "Machine Learning",
  salary: 40000
SyntaxError: Unexpected token, expected "," (23:0)

[0m [90m 21 |[39m   department[33m:[39m [32m"Machine Learning"[39m[33m,[39m
 [90m 22 |[39m   salary[33m:[39m [35m40000[39m
[31m[1m>[22m[39m[90m 23 |[39m
 [90m    |[39m [31m[1m^[22m[39m[0m
db.Teachers.insertMany([
  {
    teacher_id: 102,
    name: "Arvind",
    age: 40,
    department: "Data Science",
    salary: 45000
  },
  {
    teacher_id: 103,
    name: "Lata",
    age: 29,
    department: "Cybersecurity",
    salary: 32000
  },
  {
    teacher_id: 104,
    name: "Manoj",
    age: 37,
    department: "Machine Learning",
    salary: 40000
  }
]);
{
  acknowledged: true,
  insertedIds: {
    '0': ObjectId('68dfb41f8b9ce1c3a0b87a76'),
    '1': ObjectId('68dfb41f8b9ce1c3a0b87a77'),
    '2': ObjectId('68dfb41f8b9ce1c3a0b87a78')
  }
}
db.Teachers.insertOne({teacher_id:105,name:"jay",age:34,department:"AI",salary:35000})
{
  acknowledged: true,
  insertedId: ObjectId('68dfb4378b9ce1c3a0b87a79')
}
db.Teachers.find()
{
  _id: ObjectId('68dfb3608b9ce1c3a0b87a75'),
  teacher_id: 101,
  name: 'sheena',
  age: 34,
  department: 'AI',
  salary: 30000
}
{
  _id: ObjectId('68dfb41f8b9ce1c3a0b87a76'),
  teacher_id: 102,
  name: 'Arvind',
  age: 40,
  department: 'Data Science',
  salary: 45000
}
{
  _id: ObjectId('68dfb41f8b9ce1c3a0b87a77'),
  teacher_id: 103,
  name: 'Lata',
  age: 29,
  department: 'Cybersecurity',
  salary: 32000
}
{
  _id: ObjectId('68dfb41f8b9ce1c3a0b87a78'),
  teacher_id: 104,
  name: 'Manoj',
  age: 37,
  department: 'Machine Learning',
  salary: 40000
}
{
  _id: ObjectId('68dfb4378b9ce1c3a0b87a79'),
  teacher_id: 105,
  name: 'jay',
  age: 34,
  department: 'AI',
  salary: 35000
}
db.Teachers.findOne({name:"Manoj"})
{
  _id: ObjectId('68dfb41f8b9ce1c3a0b87a78'),
  teacher_id: 104,
  name: 'Manoj',
  age: 37,
  department: 'Machine Learning',
  salary: 40000
}
db.Teachers.find({salary:{$gt:30000}})
{
  _id: ObjectId('68dfb41f8b9ce1c3a0b87a76'),
  teacher_id: 102,
  name: 'Arvind',
  age: 40,
  department: 'Data Science',
  salary: 45000
}
{
  _id: ObjectId('68dfb41f8b9ce1c3a0b87a77'),
  teacher_id: 103,
  name: 'Lata',
  age: 29,
  department: 'Cybersecurity',
  salary: 32000
}
{
  _id: ObjectId('68dfb41f8b9ce1c3a0b87a78'),
  teacher_id: 104,
  name: 'Manoj',
  age: 37,
  department: 'Machine Learning',
  salary: 40000
}
{
  _id: ObjectId('68dfb4378b9ce1c3a0b87a79'),
  teacher_id: 105,
  name: 'jay',
  age: 34,
  department: 'AI',
  salary: 35000
}
db.Teachers.find({},{name:1,department:1,_id:0})
{
  name: 'sheena',
  department: 'AI'
}
{
  name: 'Arvind',
  department: 'Data Science'
}
{
  name: 'Lata',
  department: 'Cybersecurity'
}
{
  name: 'Manoj',
  department: 'Machine Learning'
}
{
  name: 'jay',
  department: 'AI'
}
db.Teachers.updateOne({name:"Lata"},{$set:{salary:50000,department:"Advanced Ai"}})
{
  acknowledged: true,
  insertedId: null,
  matchedCount: 1,
  modifiedCount: 1,
  upsertedCount: 0
}
db.Teachers.updateMany({department:"AI"},{$set:{salary:40000}})
{
  acknowledged: true,
  insertedId: null,
  matchedCount: 2,
  modifiedCount: 2,
  upsertedCount: 0
}
db.Teachers.deleteOne({name:"Lata"})
{
  acknowledged: true,
  deletedCount: 1
}
db.Teachers.deleteMany({salary:{$lt:30000}})
{
  acknowledged: true,
  deletedCount: 0
}
test
Selection deleted

