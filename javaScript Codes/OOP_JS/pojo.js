// object literal
// simplest way to create objects
const student = {
    name: "Rajeev",
    age: 13,
  };
  
  const student1 = {
    name: "Shubham",
    age: 13,
  };
  
  console.log(student);
  
  // javascript is a dynamic language
  // new properties can be added to ojbects at any time
  student.school = "TIME";
  
  console.log(student);
  
  // in browser console type the object name and put a .
  // note that a list of properties and methods are shown though we did not create any of them
  // these come from the underlying prototype