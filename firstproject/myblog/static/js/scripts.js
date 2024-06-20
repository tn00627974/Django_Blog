/*!
* Start Bootstrap - Clean Blog v6.0.9 (https://startbootstrap.com/theme/clean-blog)
* Copyright 2013-2023 Start Bootstrap
* Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-clean-blog/blob/master/LICENSE)
*/
// 在DOMContentLoaded事件發生時執行以下程式
window.addEventListener('DOMContentLoaded', () => {
    // 初始化變數scrollPos為0
    let scrollPos = 0;
    // 獲取id為mainNav的元素並賦值給常數mainNav
    const mainNav = document.getElementById('mainNav');
    // 獲取mainNav元素的高度並賦值給常數headerHeight
    const headerHeight = mainNav.clientHeight;
    // 當滾動事件發生時執行以下函式
    window.addEventListener('scroll', function() {
        // 獲取文檔body元素的當前位置並取負值賦值給常數currentTop
        const currentTop = document.body.getBoundingClientRect().top * -1;
        // 如果當前位置小於scrollPos則執行以下程式
        if ( currentTop < scrollPos) {
            // 向上滾動
            if (currentTop > 0 && mainNav.classList.contains('is-fixed')) {
                // 如果當前位置大於0並且mainNav元素包含class'is-fixed'，則加入class'is-visible'
                mainNav.classList.add('is-visible');
            } else {
                console.log(123);
                // 否則，移除class'is-visible'和'is-fixed'
                mainNav.classList.remove('is-visible', 'is-fixed');
            }
        } else {
            // 向下滾動
            mainNav.classList.remove(['is-visible']);
            // 如果當前位置大於headerHeight並且mainNav元素不包含class'is-fixed'，則加入class'is-fixed'
            if (currentTop > headerHeight && !mainNav.classList.contains('is-fixed')) {
                mainNav.classList.add('is-fixed');
            }
        }
        // 更新scrollPos為當前位置
        scrollPos = currentTop;
    });
})