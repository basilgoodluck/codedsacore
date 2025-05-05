class Array {
    constructor(array=[]) {
        this.array = array 
    }
    push(element){
        this.array.push(element)
    }
    pop(){
        const lastElement = this.array[this.array.length - 1]
        this.array.pop()
        return lastElement
    }
    shift(){
        const firstElement = this.array[0]
        this.array.pop()
        return firstElement
    }
    unshift(element){
        this.array.unshift(element)
    }
    length(){
        return this.array.length
    }
    index(index){
        return this.array[index]
    }
    insert(index, element){
        this.array.splice(index, 0, element)
    }
    delete(index){
        this.array.splice(index, 1)
    }
    slice(...key){
        switch(key.length){
            case 2:
                return this.array.slice(key[0], key[1])
            case 1:
                return this.array.slice(key[0])
            case 0:
                return this.array.slice()
            default:
                break
        }         
    }
}

