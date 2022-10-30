<main>
    <section class="content">
        <slot></slot>
    </section>
</main>

<style>
    main {
        display: flex;
        align-items: center;
        justify-content: center;
    }

    .content {
        width: 60%;
        margin-top: 2rem;
    }

    @media (max-width:800px) {
        .content {
            width: 80%;
        }
    }

</style>
