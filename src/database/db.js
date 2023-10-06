const mongoose = require('mongoose');
mongoose.connect('mongodb://127.0.0.1:27017/monitoreo', {
    useNewUrlParser: true,
    useUnifiedTopology: true,
}).then(()=>{
    console.log('MongoDB Conexion correcta.')
}).catch(error=>{
    console.log('Error in DB connection: ' + error)
});
// Connect MongoDB at default port 27017.