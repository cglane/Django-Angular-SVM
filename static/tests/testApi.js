var should = require('should');
var assert = require('assert');
var request = require('supertest');
var url = 'http://localhost:8000/'
// created = models.DateTimeField(auto_now_add=True, blank = True)
//   isPrimary = models.BooleanField(default = False)
//   title = models.CharField(max_length=100, blank=True, default='')
//   album = models.CharField(max_length=100, blank=True, default='Main')
//   comment = models.TextField(blank = True, default='')
//   csvFile
describe('Test me',function(){
it('Connects to User',function(done){
  request(url)
  .get('users')
  .send({'admin':'1Testing!'})
  .end(function(err,res){
    if(err)throw err;
    console.log(res.body,'body');
  })
  done()
})
it('Convert xlsv to json',function(done){
  request(url)
  .get('train_data')
  .end(function(err,res){
    if(err)throw err;
    console.log(res.body,'body');
    // res.status.should.be.equal(200);
    done()
  })
})
// it('Upload Json to fileModel',function(done){
//   request(url)
//   .post('train_data')
//   .send({"title":'my tiles','album':'album','comment':"test comment"})
//   .end(function(err,res){
//     if(err)throw err;
//     console.log(res.body,'body');
//     done()
//   })
// })
})
