// By Pedro Luis Cabrera
// Update object recursively
const util = require('util');

function customShouldDelete(val) {
    return val === null || val === undefined;
}

function removeKeyValue(obj, shouldDelete = (val) => [undefined, null, false, ''].indexOf(val) !== -1){
    if (Array.isArray(obj)){
        return obj.map((ele) => removeKeyValue(ele, shouldDelete));
    }
    if (obj && typeof obj === 'object'){
      const tempObject = Object.assign({}, obj);
      for (const key in obj){
          if (shouldDelete(obj[key])){
            delete tempObject[key];
          }else{
              tempObject[key] = removeKeyValue(obj[key], shouldDelete);
          }
      }
      return tempObject;
    }
    return obj;
}

function sortKeys(obj, order){
    if (Array.isArray(obj)){
        return obj.map((ele) => sortKeys(ele, order))
    }
    if (obj && typeof obj === 'object'){
      const tempObject = {};
      const keys = Object.keys(obj);
      keys.sort((a,b) => order === 'asc' ? a.localeCompare(b) : b.localeCompare(a));
      for (const key of keys){
           tempObject[key] = sortKeys(obj[key], order);
      }
      return tempObject;
    }
    return obj;
}

const objectOrderdBykeyAsc = sortKeys(
        [
            {
                a: 1, 
                c: 4,
                b: true,
                e: undefined,
                f: null,
                l:'',
                g: [],
                h: [
                    {a: null, k: true, j: [
                            {
                                y: false,
                                j: true,
                                m: [],
                                o: { m: false, h: true, k: [
                                        [{x:4, a: false, b: true}],{j: true, m: undefined, l: ''}
                                    ]}
                            }
                        ]}
                ],
                i: '',
            }
        ], 'desc'
    );


const objectWithUndefinedRemoved = removeKeyValue(objectOrderdBykeyAsc, customShouldDelete);
console.log(util.inspect(objectWithUndefinedRemoved, { depth: null }));





