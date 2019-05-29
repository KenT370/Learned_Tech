
function updateplot(newdata) {
    var Bar = document.getElementById('bar')
    Plotly.restyle(Bar,'x',[newdata.x])
    Plotly.restyle(Bar,'y',[newdata.y])
}
function getData(url) {
    Plotly.d3.json(`/${url}`,function(error,data){
    if (error) return console.warn(error)
    console.log('newData',data)
    updateplot(data)
    })}

