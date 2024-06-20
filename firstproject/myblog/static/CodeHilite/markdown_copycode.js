document.addEventListener('DOMContentLoaded', (event) => {
    // 找到所有的 .codehilite 區域
    var codeBlocks = document.querySelectorAll('.codehilite');

    codeBlocks.forEach(function(codeBlock) {
        // 創建複製按鈕
        var copyButton = document.createElement('button');
        copyButton.className = 'copy-button';
        copyButton.textContent = 'Copy';

        // 按下複製按鈕時的事件處理器
        copyButton.addEventListener('click', function() {
            // 獲取程式碼塊的文本
            var code = codeBlock.querySelector('code').textContent;
            
            // 創建一個臨時的textarea元素來容納文本
            var tempTextArea = document.createElement('textarea');
            tempTextArea.value = code;

            // 將textarea添加到DOM中
            document.body.appendChild(tempTextArea);

            // 選擇文本並複製到剪貼板
            tempTextArea.select();
            document.execCommand('copy');

            // 刪除臨時的textarea元素
            document.body.removeChild(tempTextArea);

            // 提示用戶已複製到剪貼板 < Ctrl + F5 清除緩除殘留 , 代碼更新才會正常>
            alert('程式碼已複製到剪貼板！');
        });

        // 將複製按鈕添加到程式碼塊的右上方
        codeBlock.appendChild(copyButton);
    });
});