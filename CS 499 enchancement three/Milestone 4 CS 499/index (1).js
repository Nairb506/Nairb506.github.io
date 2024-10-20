//defining all dependencies to be used.
var express = require("express")
var bodyParser = require("body-parser")
var mongoose = require("mongoose")

const app = express()
// tells the application to use these dependencies
app.use(bodyParser.json())
app.use(express.static('public'))
app.use(bodyParser.urlencoded({
    extended:false
}))

//establishes MondoDB connection
mongoose.connect('mongodb+srv://Ken-Admin:Cybermonkey4618@cs499db.zu6r40m.mongodb.net/?retryWrites=true&w=majority',{
    useNewUrlParser: true,
    useUnifiedTopology: true
});

//database connection variable as well as error with a console message.
var db = mongoose.connection;

db.on('error',()=>console.log("Error in Connecting to Database"));
db.once('open',()=>console.log("Connected to Database"))

//this sends a request to the html file looking for the data below and resonds with the defined values.
app.post("/employee_management_system",(req,res)=>{
    var employeeNumber = req.body.employeeNumber;
    var firstName = req.body.firstName;
    var lastName = req.body.lastName;
    var department = req.body.department;
    var accessLevel = req.body.accessLevel;
    var employmentStatus = req.body.employmentStatus;
    var salary = req.body.salary;

// this is the employee info object
    var data = {
        "employeeNumber": employeeNumber,
        "firstName" : firstName,
        "lastName": lastName,
        "department" : department,
        "accessLevel" : accessLevel,
        "employmentStatus" : employmentStatus,
        "salary" : salary
    }
    // creates the database collectiion,checks for an insertion error,and redirects back to the html file
    db.collection('employees').insertOne(data,(err,collection)=>{
        if(err){
            throw err;
        }
        console.log("Record Inserted Successfully");
    });

    return res.redirect('employee_management_system.html')

})

//allows the app to access the localhost on port 3000.
app.get("/",(req,res)=>{
    res.set({
        "Allow-access-Allow-Origin": '*'
    })
    return res.redirect('index.html');
}).listen(3000);

// outputs the listening port
console.log("Listening on PORT 3000");
