const fs = require('fs');

const createDirIfNotExists = dir => {
    if (!fs.existsSync(dir)) fs.mkdirSync(dir, { recursive: true });
}

const getYearMonth = () => {
    const currentTime = new Date();

    let month = currentTime.getMonth() + 1;
    month = ("0" + month).slice(-2);

    let year = currentTime.getFullYear();

    return [year, month];
}

hexo.extend.filter.register('new_post_path', function (data, replace) {
    data = data.split('\\');
    const file_name = data.pop();

    const new_paths = getYearMonth();
    data.push(...new_paths);
    createDirIfNotExists(data.join('\\'));

    data.push(file_name);
    data = data.join('\\');
    
    return data;
});
