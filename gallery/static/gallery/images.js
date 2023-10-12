// 모달 창 열기 및 닫기 기능 추가
var modal = document.getElementById("myModal");
var modalImg = document.getElementById("img01");

function showModal(src) {

    document.querySelectorAll(".thumbnail").forEach(img => {
        img.onclick = function() {
            modal.style.display = "block";
            modalImg.src = this.src;
        }
    });

    document.querySelector(".close").onclick = function() { 
        modal.style.display = "none";
    }

}