let person = {
    fname: "Omair",
    lname: "Shaikh",
    title: "Mr.",
  
    displayName: function () {
      console.log(`${this.title} ${this.fname} ${this.lname}`);
    },
    displayOfficialName: function () {
      console.log(`${this.lname}, ${this.fname} ${this.title}`);
    },
  };
  
  // person.displayName();
  // person.displayOfficialName();
  
  let person_1 = {
    fname: "Dinesh",
    lname: "Kumar",
    title: "Mr.",
  };
  
  let person_2 = {
    fname: "Sumit",
    lname: "Kale",
    title: "Mr.",
  };
  
  // person.displayName.call(person1);
  // person.displayName.call(person2);
  
  // person.displayName.apply(person1);
  // person.displayName.apply(person2);
  
  let person_1_FullName = person.displayName.bind(person_1);
  let persone_2_FullOfficialName = person.displayOfficialName.bind(person_2);
  
  console.log(person_1);
  console.log(person_2);
  
  console.log(person_1_FullName);
  
  person_1_FullName();
  persone_2_FullOfficialName();