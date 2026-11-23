function View(Vista, param = "") {

    const array = ["Presentation", "SignUp", "GalleryServices"];

    for (let index = 0; index < array.length; index++) {
        document.getElementsByClassName(array[index])[0].style.display = "none";
    }

    // Quitar estado activo
    document.getElementsByClassName("Rooms")[0].classList.remove("SerActive");
    document.getElementsByClassName("Consulting")[0].classList.remove("SerActive");
    document.getElementsByClassName("Equipments")[0].classList.remove("SerActive");

    document.getElementsByClassName(Vista)[0].style.display = "flex";

    document.querySelector(".GalleryServices").innerHTML = "";

    switch (param) {

        case "A1":
            document.getElementsByClassName("Rooms")[0].classList.add("SerActive");
            RoomRental();
            break;

        case "A2":
            document.getElementsByClassName("Equipments")[0].classList.add("SerActive");
            EquimentRental();
            break;

        case "A3":
            document.getElementsByClassName("Consulting")[0].classList.add("SerActive");
            ConsultingServices();
            break;
        case "A4":
            ConsultingReserves()
            break;
    }
}

document.getElementById("FormUsuario").addEventListener("submit", async (event) => {
    event.preventDefault();


        const datos = [
             document.getElementById("Identification").value,
             document.getElementById("Name").value,
             document.getElementById("Email").value,
             document.getElementById("Phone").value,
             "Register"
                ];
        
        
        response = await pywebview.api.Register(datos)

        if (response[0] && response[1] != null) {
            alert(response[1],"Bienvenido Sr(a): ", datos[1])
            LimpiarCampos()
        } else {
            alert(response[1])
        }
})

function LimpiarCampos() {
            document.getElementById("Identification").value = ""
            document.getElementById("Name").value = ""
            document.getElementById("Email").value = ""
            document.getElementById("Phone").value = ""
            document.getElementById("IdentificationUpdate").value = ""
            document.getElementById("NameUpdate").value = ""
            document.getElementById("EmailUpdate").value = ""
            document.getElementById("PhoneUpdate").value = ""
}

function ViewForms(Vista,option) {
    
    document.querySelectorAll(".SignUp form").forEach(form => {
        form.style.display = "none";
    });

    document.querySelectorAll(".UsersOptions button").forEach(button => {
        button.classList.remove("active");
    });

    document.getElementById(option).classList.add("active");
    document.getElementById(Vista).style.display = "flex";
}

document.getElementById("SeachUser").addEventListener("click", async () => 
    {
    const Identification = document.getElementById("IdentificationUpdate").value

    const response = await pywebview.api.SeachUser(Identification)
    
    if (response.length > 2) {
        document.getElementById("IdentificationUpdate").value = response[0]
        document.getElementById("NameUpdate").value = response[1]
        document.getElementById("EmailUpdate").value = response[2]
        document.getElementById("PhoneUpdate").value = response[3]
    } else {
        alert(response[1])
    }
})


document.getElementById("FormUsuario_Update").addEventListener("submit", async (event) => {
    event.preventDefault();

    const datos = [
        document.getElementById("IdentificationUpdate").value,
        document.getElementById("NameUpdate").value,
        document.getElementById("EmailUpdate").value,
        document.getElementById("PhoneUpdate").value,
        "Update"
                    ];
        
        const response = await pywebview.api.UpdateData(datos)
        
        if (response[0]) {
            alert(response[1])
            LimpiarCampos()
        } else {
            alert(response[1])
        }

})

async function ConsultingServices() {
    const consult = await pywebview.api.ConsultingService()
     const Gallery = document.querySelector(".GalleryServices");


    for (let i = 0; i < consult["Service_id"].length; i++) {
        const HourPrice = consult["Base_price"][i] - (consult["Base_price"][i] * (consult["Discount"][i] / 100));
        const Card = document.createElement("div");

        Card.classList.add("ServiceCard");

        Card.innerHTML = `
            <div class="ServiceColor"></div>

            <div class="ServiceInfo">

                <h3 class="ServiceName">
                    ${consult["Name"][i]}
                </h3>

                <p class="ServiceSpecialization">
                    ${consult["Specialization_area"][i]}
                </p>

                <p class="ServiceDescription">
                    ${consult["Description"][i]}
                </p>

                <p class="ServiceAvailability">
                    ${consult["Availability"][i] ? "Disponible" : "No disponible"}
                </p>

                <p class="ServicePrice">
                    Precio base: $${consult["Base_price"][i]}
                </p>

                <p class="ServiceDiscount">
                    Descuento: ${consult["Discount"][i]}%
                </p>

                <p class="ServicePrice">
                    Total/Hora: $<span class="FinalPrice">${HourPrice}</span>
                </p>

                <div class="ServiceSchedule">

                    <div class="ScheduleField">
                        <label>Inicio de la asesoría</label>
                        <input type="datetime-local" class="startDate">
                    </div>

                    <div class="ScheduleField">
                        <label>Fin de la asesoría</label>
                        <input type="datetime-local" class="endDate">
                    </div>

                </div>

                <button class="ReserveButton">
                    Reservar
                </button>

            </div>
        `;

        // Color aleatorio
        Card.querySelector(".ServiceColor").style.backgroundColor =
            `#${Math.floor(Math.random() * 16777215).toString(16).padStart(6, "0")}`;

        Gallery.appendChild(Card);

       const StartDate = Card.querySelector(".startDate");
        const EndDate = Card.querySelector(".endDate");
        const FinalPrice = Card.querySelector(".FinalPrice");
        const Btn_Reserva = Card.querySelector(".ReserveButton")
Btn_Reserva.style.display = "none";

function CalculateTotal() {

    // Verificar que ambas fechas estén seleccionadas
    if (!StartDate.value || !EndDate.value) {
        FinalPrice.textContent = HourPrice.toFixed(2);
        Btn_Reserva.style.display = "none";
        return;
    }

    const Start = new Date(StartDate.value);
    const End = new Date(EndDate.value);

    // Verificar que las fechas sean válidas
    if (isNaN(Start.getTime()) || isNaN(End.getTime())) {
        Btn_Reserva.style.display = "none";
        return;
    }

    // Verificar que la fecha final sea posterior a la inicial
    if (End <= Start) {
        FinalPrice.textContent = HourPrice.toFixed(2);
        Btn_Reserva.style.display = "none";
        return;
    }

    const Difference = End - Start;
    const Hours = Difference / (1000 * 60 * 60);

    const Total = HourPrice * Hours;

    FinalPrice.textContent = Total.toFixed(2);

    // Mostrar el botón cuando las fechas sean válidas
    Btn_Reserva.style.display = "grid";
}

        StartDate.addEventListener("change", CalculateTotal);
        EndDate.addEventListener("change", CalculateTotal);
        const ReserveButton = Card.querySelector(".ReserveButton");
        ReserveButton.addEventListener("click", function () {
            
        OpenReservation(consult["Service_id"][i], consult["Name"][i],consult["PriceHour"][i],consult["Availability"][i],consult["Description"][i], consult["Discount"][i], Card.querySelector(".FinalPrice").innerHTML,StartDate.value,EndDate.value, consult["TypeService"][i]);

                                                            });
    }
}

async function RoomRental() {

    const consult = await pywebview.api.Bd_RoomRental()
     const Gallery = document.querySelector(".GalleryServices");


    for (let i = 0; i < consult["Room_id"].length; i++) {
        const HourPrice = consult["PriceHour"][i] - (consult["PriceHour"][i] * (consult["Discount"][i] / 100));
        const Card = document.createElement("div");

        Card.classList.add("ServiceCard");

        Card.innerHTML = `
            <div class="ServiceColor"></div>

            <div class="ServiceInfo">

                <h3 class="ServiceName">
                    ${consult["Name"][i]}
                </h3>

                <p class="ServiceSpecialization">
                    ${consult["Furnished"][i] ? "Amoblada": "No Amoblada"}
                </p>
                <p class="ServiceSpecialization">
                   Capacidad Maxima: ${consult["Max_capacity"][i]} Personas
                </p>
                <p class="ServiceSpecialization">
                   Cantidad de salas: ${consult["Stock"][i]} 
                </p>
                <p class="ServiceDescription">
                    ${consult["Description"][i]}
                </p>

                <p class="ServiceAvailability">
                    ${consult["Availability"][i] ? "Disponible" : "No disponible"}
                </p>

                <p class="ServicePrice">
                    Precio base: $${consult["PriceHour"][i]}
                </p>

                <p class="ServiceDiscount">
                    Descuento: ${consult["Discount"][i]}%
                </p>

                <p class="ServicePrice">
                    Total/Hora: $<span class="FinalPrice">${HourPrice}</span>
                </p>

                <div class="ServiceSchedule">

                    <div class="ScheduleField">
                        <label>Inicio de la reserva</label>
                        <input type="datetime-local" class="startDate">
                    </div>

                    <div class="ScheduleField">
                        <label>Fin de la reserva</label>
                        <input type="datetime-local" class="endDate">
                    </div>

                </div>

                <button class="ReserveButton">
                    Reservar
                </button>

            </div>
        `;

        // Color aleatorio
        Card.querySelector(".ServiceColor").style.backgroundColor =
            `#${Math.floor(Math.random() * 16777215).toString(16).padStart(6, "0")}`;

        Gallery.appendChild(Card);

       const StartDate = Card.querySelector(".startDate");
        const EndDate = Card.querySelector(".endDate");
        const FinalPrice = Card.querySelector(".FinalPrice");
        const Btn_Reserva = Card.querySelector(".ReserveButton")
Btn_Reserva.style.display = "none";

function CalculateTotal() {

    // Verificar que ambas fechas estén seleccionadas
    if (!StartDate.value || !EndDate.value) {
        FinalPrice.textContent = HourPrice.toFixed(2);
        Btn_Reserva.style.display = "none";
        return;
    }

    const Start = new Date(StartDate.value);
    const End = new Date(EndDate.value);

    // Verificar que las fechas sean válidas
    if (isNaN(Start.getTime()) || isNaN(End.getTime())) {
        Btn_Reserva.style.display = "none";
        return;
    }

    // Verificar que la fecha final sea posterior a la inicial
    if (End <= Start) {
        FinalPrice.textContent = HourPrice.toFixed(2);
        Btn_Reserva.style.display = "none";
        return;
    }

    const Difference = End - Start;
    const Hours = Difference / (1000 * 60 * 60);

    const Total = HourPrice * Hours;

    FinalPrice.textContent = Total.toFixed(2);

    // Mostrar el botón cuando las fechas sean válidas
    Btn_Reserva.style.display = "grid";
}

        StartDate.addEventListener("change", CalculateTotal);
        EndDate.addEventListener("change", CalculateTotal);
        const ReserveButton = Card.querySelector(".ReserveButton");
        ReserveButton.addEventListener("click", function () {
            
        OpenReservation(consult["Room_id"][i], consult["Name"][i],consult["PriceHour"][i],consult["Availability"][i],consult["Description"][i], consult["Discount"][i], Card.querySelector(".FinalPrice").innerHTML,StartDate.value,EndDate.value, consult["TypeService"][i]);

                                                            });
    }
}

async function EquimentRental() {

    const consult = await pywebview.api.Bd_Equipment()
    const Gallery = document.querySelector(".GalleryServices");

    for (let i = 0; i < consult["Equipment_id"].length; i++) {
        const HourPrice = consult["PriceHour"][i] - (consult["PriceHour"][i] * (consult["Discount"][i] / 100));
        const Card = document.createElement("div");

        Card.classList.add("ServiceCard");

        Card.innerHTML = `
            <div class="ServiceColor"></div>

            <div class="ServiceInfo">

                <h3 class="ServiceName">
                    ${consult["Name"][i]}
                </h3>
                
                <p class="ServiceSpecialization">
                    Tipo de equipo: ${consult["TypeEquipment"][i]}
                </p>

                <p class="ServiceSpecialization">
                    ${consult["Condition"][i]}
                </p>
                <p class="ServiceSpecialization">
                   Marca: ${consult["Brand"][i]} 
                </p>
                <p class="ServiceSpecialization">
                   Cantidad Disponibles: ${consult["Stock"][i]} 
                </p>
                <p class="ServiceDescription">
                    ${consult["Description"][i]}
                </p>

                <p class="ServiceAvailability">
                    ${consult["Availability"][i] ? "Disponible" : "No disponible"}
                </p>

                <p class="ServicePrice">
                    Precio base: $${consult["PriceHour"][i]}
                </p>

                <p class="ServiceDiscount">
                    Descuento: ${consult["Discount"][i]}%
                </p>

                <p class="ServicePrice">
                    Total/Hora: $<span class="FinalPrice">${HourPrice}</span>
                </p>

                <div class="ServiceSchedule">

                    <div class="ScheduleField">
                        <label>Inicio de la reserva</label>
                        <input type="datetime-local" class="startDate">
                    </div>

                    <div class="ScheduleField">
                        <label>Fin de la reserva</label>
                        <input type="datetime-local" class="endDate">
                    </div>

                </div>

                <button class="ReserveButton">
                    Reservar
                </button>

            </div>
        `;

        // Color aleatorio
        Card.querySelector(".ServiceColor").style.backgroundColor =
            `#${Math.floor(Math.random() * 16777215).toString(16).padStart(6, "0")}`;

        Gallery.appendChild(Card);

        const StartDate = Card.querySelector(".startDate");
        const EndDate = Card.querySelector(".endDate");
        const FinalPrice = Card.querySelector(".FinalPrice");
        const Btn_Reserva = Card.querySelector(".ReserveButton")
Btn_Reserva.style.display = "none";

function CalculateTotal() {

    // Verificar que ambas fechas estén seleccionadas
    if (!StartDate.value || !EndDate.value) {
        FinalPrice.textContent = HourPrice.toFixed(2);
        Btn_Reserva.style.display = "none";
        return;
    }

    const Start = new Date(StartDate.value);
    const End = new Date(EndDate.value);

    // Verificar que las fechas sean válidas
    if (isNaN(Start.getTime()) || isNaN(End.getTime())) {
        Btn_Reserva.style.display = "none";
        return;
    }

    // Verificar que la fecha final sea posterior a la inicial
    if (End <= Start) {
        FinalPrice.textContent = HourPrice.toFixed(2);
        Btn_Reserva.style.display = "none";
        return;
    }

    const Difference = End - Start;
    const Hours = Difference / (1000 * 60 * 60);

    const Total = HourPrice * Hours;

    FinalPrice.textContent = Total.toFixed(2);

    // Mostrar el botón cuando las fechas sean válidas
    Btn_Reserva.style.display = "grid";
}

        StartDate.addEventListener("change", CalculateTotal);
        EndDate.addEventListener("change", CalculateTotal);
        const ReserveButton = Card.querySelector(".ReserveButton");
        ReserveButton.addEventListener("click", function () {
            
        OpenReservation(consult["Equipment_id"][i], consult["Name"][i],consult["PriceHour"][i],consult["Availability"][i],consult["Description"][i], consult["Discount"][i], Card.querySelector(".FinalPrice").innerHTML,StartDate.value,EndDate.value, consult["TypeService"][i]);

                                                            });
    }
}

function OpenReservation(ID, Name, PriceHour, Availability, Description, Descuento, Total, StartDate, EndDate, TypeService) {

    const PopUp = document.querySelector(".pop_up");

    PopUp.innerHTML = `
        <div class="ReservationWindow">

            <h2 class="ReservationTitle">
                Confirmar reserva
            </h2>

            <div class="ReservationInfo">
                <p>
                    <strong>Digite su identificacion:</strong>
                    <input class="ID_recibo" type="number">
                </p>

                <p>
                    <strong>Nombre:</strong>
                    ${Name}
                </p>

                <p>
                    <strong>Precio por hora (Incluye Impuestos):</strong>
                    $${PriceHour}
                </p>

                <p>
                    <strong>Descuento:</strong>
                    ${Descuento}%
                </p>

                <p>
                    <strong>Total:</strong>
                    $${Total}
                </p>

                <p>
                    <strong>Disponibilidad:</strong>
                    ${Availability ? "Disponible" : "No disponible"}
                </p>

                <p>
                    <strong>Descripción:</strong>
                    ${Description}
                </p>
            </div>

            <div class="ReservationDates">

                <div class="ReservationDate">

                    <label>
                        Inicio
                    </label>

                    <input
                        type="datetime-local"
                        value="${StartDate}"
                        readonly
                    >

                </div>

                <div class="ReservationDate">

                    <label>
                        Finalización
                    </label>

                    <input
                        type="datetime-local"
                        value="${EndDate}"
                        readonly
                    >

                </div>

            </div>

            <div class="ReservationButtons">

                <button
                    class="CancelReservation"
                    id="CancelReservation">
                    Cancelar
                </button>

                <button
                    class="GenerateReservation"
                    id="GenerateReservation">
                    Generar Reserva
                </button>

            </div>

        </div>
    `;

    PopUp.style.display = "flex";

    document
        .getElementById("CancelReservation")
        .addEventListener("click", function () {

            PopUp.style.display = "none";
            PopUp.innerHTML = "";

        });


    // Guardamos las dos fechas
    const Tiempo = [StartDate, EndDate];


    document
        .getElementById("GenerateReservation")
        .addEventListener("click", async function () {

            // Obtener la identificación escrita por el usuario
            const ID_User = document.querySelector(".ID_recibo").value;

            switch (TypeService) {

                case "Renta Salas":
                    TypeService = "RoomRental";
                    break;

                case "Renta Equipos":
                    TypeService = "EquipmentRental";
                    break;

                case "Asesoria":
                    TypeService = "ConsultingServices";
                    break;

                default:

                    alert("Error: Categoria de servicio no encontrada"," - ",TypeService);
                    return;
            }
            const response = await pywebview.api.GenerateReservation(
                ID_User,
                ID,
                TypeService,
                Tiempo
            );

            alert(response[1]);

            PopUp.style.display = "none";
            PopUp.innerHTML = "";
        });
}


async function ConsultingReserves() {
    const Consult = await pywebview.api.GetReservation();

    const Section = document.querySelector(".GalleryServices");

    let HTML = `
        <table class="ReservationTable">
            <thead>
                <tr>
                    <th>ID Reserva</th>
                    <th>Usuario</th>
                    <th>ID Servicio</th>
                    <th>Nombre</th>
                    <th>Servicio</th>
                    <th>Duración</th>
                    <th>Tiempo Servicio</th>
                    <th>Estado</th>
                    <th>Total</th>
                    <th>Cancelar</th>
                    <th>Reservar</th>
                </tr>
            </thead>
            <tbody>
    `;

    for (let i = 0; i < Consult.ID_Reservation.length; i++) {
        HTML += `
            <tr>
                <td>${Consult.ID_Reservation[i]}</td>
                <td>${Consult.User[i]}</td>
                <td>${Consult.IDService[i]}</td>
                <td>${Consult.Name[i]}</td>
                <td>${Consult.Service[i]}</td>
                <td>${Consult.Duration[i]}</td>
                <td>${Consult.TimeService[i].join(" / ")}</td>
                <td>
                    <span class="ReservationState">
                        ${Consult.State[i]}
                    </span>
                </td>
                <td>${Consult.Total[i]}</td>
                <td>
                    <button class="BtnCancel"
                        onclick="CancelReservation(${Consult.ID_Reservation[i]})">
                        Cancelar
                    </button>
                </td>
                <td>
                    <button class="BtnReserve"
                        onclick="MakeReservation(${Consult.ID_Reservation[i]})">
                        Reservar
                    </button>
                </td>
            </tr>
        `;
    }

    HTML += `
            </tbody>
        </table>
    `;

    Section.innerHTML = HTML;
}

