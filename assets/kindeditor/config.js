KindEditor.ready(function (K) {
    window.editor = K.create('textarea', {
        width: '550px',
        minWidth: '550px',
        height: '600px',
        resizeType: 1,
        items: [
            'formatblock', 'fontname', 'fontsize', '|',
            'forecolor', 'bold', 'italic', 'underline', 'strikethrough', 'lineheight', 'removeformat', '|',
            'image', 'multiimage', 'insertfile', 'table', 'hr', 'emoticons', '|',
            'preview', 'print', '|',
            'justifyleft', 'justifycenter', 'justifyright', 'justifyfull', 'insertorderedlist', 'insertunorderedlist', 'indent', 'outdent', 'quickformat', 'selectall', 'link', 'unlink', '/',
            'undo', 'redo', 'fullscreen'],
        themeType: 'simple',
        uploadJson: '/api/richtext/media/upload/',
        fullscreenShortcut: true,
        extraFileUploadParams: {},
        filePostName: 'file',
        autoHeightMode: true,
        cssData: 'body {font-family: "宋体"; font-size: 14px}',
        fillDescAfterUploadImage: true,
        urlType:'domain' // Note: Related implement in kindeditor-all.js has been commented.key: keyword-urlType
    });
});
